#Budget Tracker Application

class Transaction:
    def __init__(self, budget = None):
        self.budget = budget
        self.listIncomes = []
        self.expensesDict = {}

    #ask for incomes
    def incomes(self):  
        numberIncomes = 0
        print('press 0 to exit')
        while self.budget != 0:
            try:
                numberIncomes += 1
                self.budget = float(input('what is the amount income : '))
                print('-'* 20)
                self.listIncomes.append(self.budget)
                
            except ValueError:
                print('Please enter a number')
 
        budgetSum = sum(self.listIncomes)
        
        return f'the sum of your incomes {budgetSum}'
    
    def expenses(self):
        print("""           
                    1 : Rent/Mortgage
                    2 : Food/Groceries
                    3 : Utilities
                    4 : Transportation
                    5 : Healthcare
                    6 : Debt Payments
                    7 : Personal Care
                    8 : Internet/Phone""")
        print('press enter to exit')
        expensesDict = {
            1 : 'Rent/Mortgage', 2 : 'Food/Groceries', 3 : 'Utilities', 4 : 'Transportation', 5 : 'Healthcare', 
                        6 : 'Debt Payments', 7 : 'Personal Care', 8 : 'Internet/Phone'
        }
        try:
            for item in range(len(expensesDict)):            
                expensesName, expensesAmount = input('what is your expense : '), float(input('what is the amount of the expense : '))
 
        except ValueError as e:
            print('Please enter a number between 1 and 8')
            if expensesName not in range(8):
                raise(e)
        return self.expensesDict
        
    
    #add budget
    def addBudget(self):
        pass
    
    
    
    
    #view budget
    def viewBudget(self):
        pass
    
a = Transaction()
print(a.expenses())