# Deleting Items:
# Remove a key-value pair from the dictionary using the del keyword.


# initializing empty dictionary
dic={}
# asking user how many enteries he want to add
ask=int(input("How many dishes you want to add?:"))
# applying loop for taking user input
for i in range(1,ask+1):
    dish_name=input("Enter your Dish Name:")
    price=int(input("Enter your Desired Price:"))
    dic.update({dish_name:price})
print("You Enter The Items:")
print()
# initializing empty list so taking all users entered item in list 
user=[]
# applying loop on both key value pair to append in list
for i in dic.items():
    user.append(i)
# printing list items in standard form
for i in user:
    for j in i:
        print(j,end=" ")
    print()
print()
# asking user which item he want to remove from list
ask=input("Which key value pair you want to remove from list?:")
# converting all in lower case
ask=ask.lower()
# initializing another empty list
final=[]
# initial check=false
check=False
# applying loop for removing item what user want
for i in dic:
    if i==ask:
        # using del for removing key value pair
        del dic[ask]
        # declaring check ==true
        check=True
        # appending all item in final list
        for i in dic.items():
            final.append(i)
        break 

# if check==true so printing modified list in standard form
if check:
  print("Your Modified List:")
  print()
  for i in final:
   for j in i:
        print(j,end=" ")    
   print()
else:
    print("There Is No Item Of That Key")
    