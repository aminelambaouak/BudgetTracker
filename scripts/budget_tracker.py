#Budget Tracker Application
import json
import mysql.connector

class BudgetTracker:
    def __init__(self,  budget= None):
        self.budget = budget
        self.expensesDict = {}
        self.AmountsDict = {}
        self.data = {}
        
    #ask for incomes
    def incomes(self):  
        print("Welcome to Budget Tracker")
        print('-'*50)
        print('press 0 when no source to add')
        print('-'*50)
        while True:
            try: 
                incomeCategory = input('income category : ')  
                budgetAmount = float(input('what is the income amount (0 to stop): '))
                if budgetAmount == 0:
                    break
                elif budgetAmount < 0:
                    print("Please enter a positive number.")
                else:

                    if incomeCategory in self.AmountsDict:
                        self.AmountsDict[incomeCategory] += budgetAmount
                    else:
                        self.AmountsDict[incomeCategory] = budgetAmount
            except ValueError:
                print('Please enter a number')
            if incomeCategory.isdigit():
                print("Error: Please enter text, not a number for income category.")
            else:
                continue

        print(self)
    # Expenses function to calculate the sum of user's expenses
    def expenses(self):
        #Tell the user to press 0 to exit
        while True:
            try:
                expenseCategory = input('expense category: ')
                expenseAmount = float(input("Enter expense amount (0 to stop): "))
                if expenseAmount == 0:
                    break
                elif expenseAmount < 0:
                    print("Please enter a positive number.")
                else:

                    if expenseCategory in self.expensesDict:
                        self.expensesDict[expenseCategory] += expenseAmount
                    else:
                        self.expensesDict[expenseCategory] = expenseAmount
            except ValueError:
                print('Please enter a real number')
                
            if expenseCategory.isdigit():
                print("Error: Please enter text, not a number for expense category.")
            else:
                continue

        print(self)
    # calculate the balance
    def getBalance(self):
        balance = sum(self.AmountsDict.values()) - sum(self.expensesDict.values())
        return balance
    # print a string 
    def __str__(self):
        if sum(self.expensesDict.values()) == 0:
            return f'total income : {sum(self.AmountsDict.values()):.2f}'
        elif sum(self.AmountsDict.values()) == 0:
            return f'total expenses : {sum(self.expensesDict.values()):.2f} and balance : {self.getBalance():.2f}'
        else:
            return f""" 
                        Incomes : {self.AmountsDict}
                        total income : {sum(self.AmountsDict.values()):.2f}
                        expenses : {self.expensesDict}
                        total expenses :  {sum(self.expensesDict.values()):.2f}
                        balance : {self.getBalance():.2f}"""
    # Extract the data in JSON file
    def extractData(self):
        data = {
            "income": self.AmountsDict,
            "expenses": self.expensesDict,
            "balance" : self.getBalance()
        }
        with open("budget_data.json", "w") as file:
            json.dump(data, file)
                
        with open("budget_data.json", "r") as file:
            loaded_data = json.load(file)
            print('Your data = ', loaded_data)
    # Load the data collected in mysql database
    def database(self):
        # Connect to database (it will create one if it doesn't exist)
        mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="070193",
                        database = 'BudgetTracker'
                        )
        myCursor = mydb.cursor()
        # Create the new database if it does not exist
        myCursor.execute("CREATE DATABASE IF NOT EXISTS BudgetTracker")

        # Confirm that the database was created by listing the databases
        myCursor.execute("SHOW DATABASES")
        # Fetch and print the databases
        for db in myCursor:
            print(db)
        # Create a cursor object to execute SQL commands
        myCursor.execute('''CREATE TABLE IF NOT EXISTS my_balances (  income_category VARCHAR(20),
                                                                    income_amount REAL,
                                                                    expense_category VARCHAR(20),
                                                                    expense_amount REAL);''')
        # Insert income entries (with NULL for expense columns)
        for category, amount in self.AmountsDict.items():
            myCursor.execute(
                "INSERT INTO my_balances (income_category, income_amount, expense_category, expense_amount) VALUES (%s, %s, %s, %s)",
                (category, amount, None, None)
            )
        # Insert expense entries (with NULL for income columns)
        for category, amount in self.expensesDict.items():
            myCursor.execute(
                "INSERT INTO my_balances (income_category, income_amount, expense_category, expense_amount) VALUES (%s, %s, %s, %s)",
                (None, None, category, amount) 
            )
        mydb.commit()
        # Close connection
        myCursor.close()

a = BudgetTracker()
print(a.incomes())
print(a.expenses())
print(a.extractData())
print(a.database())