# Certainly! Let's try a slightly more challenging task:

# Task: Contact Management System
# Write a Python program for a simple contact management system. The program should perform the following steps:

# Allow users to add new contacts with the following information: name, phone number, and email address.
# Implement a search feature that allows users to search for a contact by name and display their details.
# Implement an update feature that allows users to update the phone number or email address of an existing contact.
# Allow users to delete a contact.
# # Display the complete list of contacts with their details.

print("There is a simple contact mangement system for you")
print("You can add,update,delete,display or end the program")
print()
array=[]         #making an emptylist
while True:        #applying loop for overall code
    while True:     #applying loop for choices
     choice=input("Enter Your Choice:[add/update/delete/display/end]:")
     choice=choice.lower()
     if choice=="add" or choice=="update" or choice=="delete" or choice=="display" or choice=="end":
        break
     else:
        print("Please Enter correct word")
    if choice=="add":        #applying condition now
        name=input("Enter Name of person:")
        contact=input("Enter contact no of person:")
        email=input("Enter Email of person:")
        details={"name":name,"contact":contact,"email":email}   #making adictionary
        array.append(details)    #appending usersinput in dic and then in list
        print("Your Data:")
        for i in array:     #printing data in standard form
            for j in i.items():
                for k in j:
                    print(k,end=" ")
                print()
            print()
    elif choice=="update":
        array
        key=input("Which key value You want to update?:")
        key=key.lower()      #converting in lower
        data=input("Enter corresponding data related to key:")
        write=input("What you want to write in replacement?: ")
        found=False      #initial false
        for check in array:      
            if check.get(key)==data:       #checking if keyvalue==data
                check.update({key:write})   #if cond true then updating in dic 
                found=True                #initial to true
        if found:                       #printing in standard form
          for i in array:
             for j in i.items():
                 for k in j:
                    print(k,end=" ")
                 print()
             print()
        else:
            print("You Entered wrong key")
           
        found=False       
    elif choice=="delete":
        array
        key=input("Whick key value You want to delete?:")
        data=input("Enter corresponding data related to key:")
        for check in array:
            if check.get(key)==data:
                del check[key]
                found=True
        if found:
            for i in array:
                for j in i.items():
                    for k in j:
                        print(k,end=" ")
                    print()
                print()
        else:
            print("you entered wrong key")
        found=False
    elif choice=="display":
        array
        fix="name"         #fix the search name by name
        search=input("Enter the name to display: ")     #asking user to enter name
        for check in array:
            if check.get(fix)==search:      
                found=True
        if found:
             print(check.get("name"))
             print(check.get("contact"))
             print(check.get("email"))        #printing values
        else:
            print("You Entered Wrong Name")
    
    elif choice=="end":        #finishing program
        for i in array:
            for j in i.items():
                for k in j:
                    print(k,end=" ")
                print()
            print()
        break                  #break out of loop

                




        





























# array=[]
# while True:
#     name=input("Enter name:")
#     name=name.lower()
#     if name=="end":
#         break
#     else:
#         contact=int(input("Enter Your Contact No:"))
#         email=(input("Enter Your Email Address:"))
#         details={"name":name,"Contact":contact,"Email":email}
#         array.append(details)
# print(array)
# sett="name"
# ask=input("Enter The name:")
# for check in array:
#     if check.get(sett)==ask:
#         print(check.get(ask))
#         print(check.get("Contact"))
#         print(check.get("Email"))
        
















# l=[]       
# # ask="name"
# # search=input("Enter The name:")
# a=[{"name":"raza","class":"eight","height":12},{"name":"ahmed","class":"nine","height":14}]
# print(a)
# ask=input("Enter Which key:")
# enter=input("Enter corresponding data:")
# write=input("Enter to write::")
# for check in a:
#     if check.get(ask)==enter:
#       check.update({ask:write})
# print(a)
     






# for dic in a:
    # if dic.get(ask)==search:
    #     print(dic.get(ask))
    #     print(dic.get("class"))
    #     print(dic.get("height"))


# for i in a:
#     for j in i:
#         if j==ask:
#             print(i.get("name"))
#             print(i.get("class"))
#             print(i.get("height"))
#             if i=="name":
            
  
#   for i in a:
#     print(i.get("name"))
   