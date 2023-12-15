# Search for an Element:
# Write a function that takes an element as input and returns True if it's present in the 2D list, False otherwise.


# initializing empty list to append user input in it
final=[]
# applying loop for taking users input
for i in range(3):
  user_input=input("Enter List seperated by spaces row wise:")
  user_input=user_input.split()
  user_input=[int(i)for i in user_input]
  final.append(user_input)
# printing the users data in standard form

print("You Entered these numbers:")
print()
for i in final:
  for j in i:
    print(j,end=" ")
  print()
print()
# asking user which element he wants to check
ask=int(input("Enter Which number you want to check:"))
# initializing found=false
found=False
# applying condition to check users input in list or not
for check in final:
  if ask in check:
    found=True
    break
# printing if find an element
if found:
  print("True")
else:
  print("False")