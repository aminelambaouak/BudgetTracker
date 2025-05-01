#Budget Tracker Application
import pandas as pd
import json

class BudgetTracker:
    def __init__(self,  budget= None):
        self.budget = budget
        self.expensesDict = {}
        self.AmountsDict = {}
    #ask for incomes
    def incomes(self):  
        print("Welcome to Budget Tracker")
        print('-'*50)
        print('press 0 when no source to add')
        print('-'*50)
        while True:
            try: 
                self.Income = input('what is your income : ')  
                self.budget = float(input('what is the income amount (0 to stop): '))
                if self.budget == 0:
                    break
                elif self.budget < 0:
                    print("Please enter a positive number.")
                else:

                    if self.Income in self.AmountsDict:
                        self.AmountsDict[self.Income] += self.budget
                    else:
                        self.AmountsDict[self.Income] = self.budget
            except ValueError:
                print('Please enter a number')

        print(self)
    # Expenses function to calculate the sum of user's expenses
    def expenses(self):
        #Tell the user to press 0 to exit
        while True:
            try:
                expenseCategory = input('what is the expense category: ')
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
                    
    def extractData(self):
        data = {
            "income": self.AmountsDict,
            "expenses": self.expensesDict
        }
        with open("budget_data.json", "w") as file:
            json.dump(data, file)
                
        with open("budget_data.json", "r") as file:
            loaded_data = json.load(file)
            print('Your data = ', loaded_data)
     

    
a = BudgetTracker()
print(a.incomes())
print(a.expenses())
print(a.extractData())