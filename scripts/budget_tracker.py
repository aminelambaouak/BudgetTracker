#Budget Tracker Application

class Transaction:
    def __init__(self,  budget = None):
        self.budget = budget
        self.listIncomes = []
        self.expensesList = []
    #ask for incomes
    def incomes(self):  
        numberIncomes = 0
        print("Welcome to Budget Tracker")
        print('-'*50)
        print('press 0 when no source to add')
        print('-'*50)
        while True:
            if self.budget != 0:
                
                try:
                    numberIncomes += 1
                    self.budget = float(input('what is the amount income : '))
                    self.listIncomes.append(self.budget)
                    
                except ValueError:
                    print('Please enter a number')
            else:
                break
        print(self)
    # Expenses function to calculate the sum of user's expenses
    def expenses(self):
        #Tell the user to press 0 to exit
        while True:
            try:
                expenseCategory = input('what is the expense : ')
                expenseAmount = float(input("Enter income (0 to stop): "))
                if expenseAmount == 0:
                    break
                elif expenseAmount < 0:
                    print("Please enter a positive number.")
                else:
                    self.expensesList.append(expenseAmount)
            except ValueError:
                print('Please enter a real number')
        print(self)
        
    def getBalance(self):
        balance = sum(self.listIncomes) - sum(self.expensesList)
        return balance
    # print a string 
    def __str__(self):
         return f'The sum of your expenses is : {sum(self.expensesList):.2f}, total income : {sum(self.listIncomes):.2f} and the balance : {self.getBalance():.2f}'

    
a = Transaction()
print(a.incomes())
print(a.expenses())