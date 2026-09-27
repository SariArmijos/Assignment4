#Personal Expense Analyzer

#Create lists for small, moderate and large expenses
small_expenses = []
moderate_expenses = []
large_expenses = []
#Create list for all expenses
all_expenses = []

#Ask the user to enter their expenses, when they are done they should enter 0
expense = float(input('Enter an expense or 0 to finish: '))
#Once user has inserted expense take them into the loop
while expense != 0 : 
    #Make sure user inserts a valid number (not negative)
    #If the user inserts a negative number, take them to a loop and ask them to insert a valid one
    if expense < 0 :
        #If the user inserts a negative number, ask to insert a valid one 
        print('Please, enter a valid expense (not negative)')
        expense = float(input('Enter an expense or 0 to finish: '))
    #If it is a valid number then clasify each expense
    else : 
        #Add expense to all_expenses list
        all_expenses.append(expense)
        #Start expense count
        expense_count = 0
        #If expense < 25 then add it to the small_expenses list
        if expense < 25 :
            small_expenses.append(expense)
        #If expense <= 100 then add it to the moderate_expenses list
        elif expense <= 100 :
            moderate_expenses.append(expense)
        #If expense > 100 then add it to the large_expenses list
        else :
            large_expenses.append(expense)
        #Keep track of the expenses
        expense_count += 1
        #Ask the user to keep adding expenses or exit the loop
        expense = float(input('Enter an expense or 0 to finish: '))
        
#Print a break
print('\n')
#Print total expenses
print('total expenses'.upper()) 
#Print a break
print('\n')

#From here I will format numbers as currency and make sure to sure f to combine strings with numbers
#Total number of expenses
print(f'Number of expenses: {len(all_expenses)}')

#Make sure that numbers are presented and rounded up to 2 decimals (:.2f)
#Total expenses. Use the sum function to add all expenses from the all_expenses list
print(f'Total: ${sum(all_expenses):.2f}')

#Average expense. Since there is not an average function built in Python I had to use a formula
#To calculate average is total expenses/number of expenses
print(f'Average: ${(sum(all_expenses)/len(all_expenses)):.2f}')

#Smallest expense. Use min function to find the smallest expense from the total list
print(f'Smallest expense: ${min(all_expenses):.2f}')

#Largest expense. Use max function to find the smallest expense from the total list
print(f'Largest expense: ${max(all_expenses):.2f}')

#Print a break
print('\n')

#Number of small, medium and large expenses
#Use len functio to count expenses from each list
print(f'Small expenses: {len(small_expenses)}')
print(f'Moderate expenses: {len(moderate_expenses)}')
print(f'Large expenses: {len(large_expenses)}')

#Print a break
print('\n')