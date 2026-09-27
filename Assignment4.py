#Personal Expense Analyzer

#Ask the user to enter their expenses, when they are done they should enter 0
expense = float(input('Enter an expense or 0 to finish: '))
#Once user has inserted expense take them into the loop
while expense != 0 : 
    #Make sure user inserts a valid number (not negative)
    #If the user inserts a negative number, take them to a loop and ask them to insert a valid one
    while expense < 0 :
        #If the user inserts a negative number, ask to insert a valid one 
        print('Please, enter a valid expense (not negative)')
        expense = float(input('Enter an expense or 0 to finish: '))
    #If it is a valid number then clasify each expense
    #Start expense count
    expense_count = 0
    #Create lists for small, moderate and large expenses
    small_expenses = []
    moderate_expenses = []
    large_expenses = []
    #Create list for all expenses
    all_expenses = []
    while expense != 0 :
        #If expense < 25 then add it to the small_expenses list
        if expense < 25 :
            small_expenses += expense
        #If expense <= 100 then add it to the moderate_expenses list
        elif expense <= 100 :
            moderate_expenses += expense
        #If expense > 100 then add it to the large_expenses list
        else :
            large_expenses += expense
        #Add each expense list to a total list
        all_expenses += small_expenses, moderate_expenses, large_expenses
        #Keep track of the expenses
#Print total expenses
#Total number of expenses
#Total expenses
#Average expense
#Smallest expense
#Largest expense
#Number of small, medium and large expenses
#I am making changes here