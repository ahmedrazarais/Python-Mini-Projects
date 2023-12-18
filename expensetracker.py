
# Absolutely! Here's another task for you:

# Task: Personal Expense Tracker

# Write a Python program that helps users keep track of their personal expenses. The program should perform the following steps:

# Ask the user to enter the name of the expense (e.g., "Groceries," "Gas," "Entertainment").
# Ask the user to enter the amount spent on that expense.
# Store the expenses in a dictionary, where the expense names are keys, and the amounts are values.
# Allow the user to keep adding expenses until they enter "done" to finish.
# After the user is done entering expenses, display the complete list of expenses with their corresponding amounts.
# Calculate and display the total amount spent.


print("update your expense and amount to be spend on that task simply write done if you want to exit")
expense_dic={}
while True:
    expense=input("Enter name of expense:")
    expense=expense.lower()
    if expense=="done":
        break
    else:
        price=int(input("Enter amount spent on that task:"))
        expense_dic.update({expense:price})
print("Your Complete respose:")
print("EXPENSE :  AMOUNT")
for check in expense_dic.items():
    for i in check:
        print(i,end=" ")
    print()
total=[]
for i in expense_dic.values():
    total.append(i)
result=sum(total)
print(f"The Total amount yopu spend on expenses are {result}")

     