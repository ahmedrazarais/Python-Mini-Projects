# Add a new key-value pair to the dictionary if user want
# Flower name must be key and flower color must be key value as we discuseed in class
# Dont handle that case if user enter more than 1 same key as you are beginner

# initializing empty dictionary
dic={}
# asking user how many enteries he want to do
ask=int(input("Enter How many enteries yoou want to do ?:"))
# applying loop for taking user input
for i in range(1,ask+1):
    fvt_flr=input("Enter Your favourite flower name:")
    fvt_clr=input("Enter Your favourite flower colour:")
    # converting all values of user in dic in key value form
    dic.update({fvt_flr:fvt_clr})
# printing user_dictionary    
print(f"Your dictionary is:{dic}")
print()
# asking user if he want to add more items?
user_ask=input("Did You want to add more key value pairs?[yes/no]:")
print()
# converting in lower case
user_ask=user_ask.lower()
# checking if user say yes or no
if user_ask=="yes":
    # asking user how many values he want to add more
    quantity=int(input("How many more key value pair you want to add?:"))
    # applying loop again for taking user input
    for i in range(1,quantity+1):
        fvt_flr=input("Enter Your favourite flower name:")
        fvt_clr=input("Enter Your favourite flower colour:")
        dic.update({fvt_clr:fvt_flr})
    # printing modified dictionary of user
    print(f"Your Modified dictionary is {dic}")    
else:
    print(f"so your dictionary without any change is {dic} ")