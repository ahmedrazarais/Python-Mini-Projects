# Updating Values:
# Change the value associated with a specific key.
# initializing empty dictionary
dic={}
# printing information to user:
print("Enter data as much as you want to enter just write Q or q in name when you finished")
# applying loop for taking user input
while True:
    name=input("Enter Name Of Student:")
    if name=="Q" or name=="q":  
        break
    else:
       roll_no=input("Enter roll_no Of Student:")
       dic.update({roll_no:name})
# printing entire dictionary to user       
print(f"Your Dictionary Is:{dic}")
print()
# asking user whicc key value he want to change
ask=input("which key value you want to change?:")
write=input("What You Want to write in replacement?:")
# applyintg loop for checking conditions
for i in dic:
    if i==ask:
        dic.update({ask:write})
        print(f"your Modified Dictionary is : {dic}")
        break
else:
    print("There Is No Key Of That Name")

