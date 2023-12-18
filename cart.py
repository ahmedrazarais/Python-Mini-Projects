# Task: Shopping List Organizer

# Write a Python program that helps users organize their shopping list. The program should perform the following steps:

# Ask the user to enter items they want to buy, one at a time, until they enter "done" to finish the list.
# For each item, ask the user to enter the quantity they want to buy.
# Store the items and quantities in a dictionary, where the item names are keys, and the quantities are values.
# After the user is done entering items, display the complete shopping list with items and quantities.
# Make use of strings, integers, dictionaries, and loops to implement this program.


print("Making your desired shopping cart when you want to finish shopping simply write done")
menu={}          #making an empty dic
while True:
    item=input("Enter Your Item What you want to add:")   #takinguserinput
    item=item.lower()     #converting all lower
    if item=="done":     #conditions for break
        break
    else:
        quantity=int(input("Enter The quantity  Of item:"))       #quantity asking
        menu.update({item:quantity})     #converting in dic
print("Your Shopping List is:")     #printing shopping list
print("ITEMS : QUANTITY")
for items in menu.items():
    for i in items:
        print(i,end=" ")
    print()
