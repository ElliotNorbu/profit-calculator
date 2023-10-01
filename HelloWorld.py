month = str(input("enter month:"))
print("income statement for the" ,month)
income= int(input("enter income for the month:"))
expense=int(input("enter expense for the month:"))
tax=int(input("enter tax for the month:"))
totalExpense= expense + tax
profit= income - totalExpense
print("Your profit is" ,profit)