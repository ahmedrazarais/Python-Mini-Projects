
# 4. Write Python program to input and store  integer values from user. User can input as many values as
# s/he wants separated by spaces; presses enter to quit. Ignore any other invalid entries; do not write them to file. Ask
# user if s/he wants to see the contents of the file at the end.

while True:
  values=input("Enter The Integers seperated by spaces:")
  values=values.split()    # splitting for making list
  break

# Opening afile that aready created
user_info=open("C:/Users/ideal pc/Desktop/ComuterProgramming/ComputerProgramming/user.txt","w+")
# applying loop on list
for check in values:
  if check.isdigit():       # apply cond to remove invalid enteries
    result=check
    user_info.write(check + " ")         #write user values in file

choice=input("Did You Want to see the file?: press yes or no :")    #asking to see file
choice=choice.lower()
if choice=="yes":      
  user_info.seek(0)        # seek bcz when we write cursor it at last word so we seek to first
  print(f" You entered these values :{user_info.read()}")         #printing user file
else:
  print("Alright")