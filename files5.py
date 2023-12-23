# # 5. Implement function duplicate that takes as input the name (a string) of a file in the current directory and returns
# # True if the file contains duplicate words and False otherwise.

# file="C:/Users/ideal pc/Desktop/ComuterProgramming/ComputerProgramming/duplicate.txt"
# def duplicate(file):
#     file=open(file)

#     x=file.read()
#     words=[x[i:i+1] for i in range(0,len(x))]
#     found=False
#     for check in words:
#         if x.count(check)!=1:
#             found=True
#     if found:
#         print("True")
#     if not found:
#         print("false")
#     file.close()
# duplicate(file)
# print("welcome to raba house")
# print("\t1.signup")
# print("\t2.Login")
# while True:
#     choice=input("Enter Your choice:")
#     if choice==1 or choice==2:
#         break
#     else:
#         print("Please Enter Correct choice")




# user_info="C:/Users/ideal pc/Desktop/ComuterProgramming/ComputerProgramming/filing.txt"
# def signup(user_info):
#     user_info=open(user_info,"a+")
#     fst_name=input("Enter Your First name:")
#     last_name=input("Enter Your last name:")
#     unique=input("Enter Id:")
#     address=input("Enter Your Adress:")
#     user_info.seek(0)
#     found=False
#     for i in user_info.readlines():
#         if unique in i:
#             found=True
#     if found:
#         print("You have already an account  account already please login")
#     else:
#         print("Signup successfully")
#         user_info.write(f"{unique}\n")
#         user_info.write(f"{address}\n")

#     user_info.close()
# # signup(user_info)

# user_info="C:/Users/ideal pc/Desktop/ComuterProgramming/ComputerProgramming/filing.txt"
# def login(user_info):
#     user_info=open(user_info)
#     name=input("Enter Your name:")
#     id=input("Enter Your id:")
#     found=False
#     for i in user_info.readlines():
#         if id in i:
#             found=True     
#     if found:
#         print("Login complete")
#     else:
#         print("Incorrect id")


# print("welcome to raba house")
# print("\t1.signup")
# print("\t2.Login")
# while True:
#     while True:
#        choice=int(input("Enter Your choice:"))
#        if choice==1 or choice==2:
#           break
#        else:
#          print("Please Enter Correct choice")
#     if choice==1:
#         signup(user_info)
#     elif choice==2:
#         login(user_info)
    

#     ask=input("Did You want to continue?: yes or no :")
#     ask=ask.lower()
#     if ask in "no":
#         break









# Student Database:

# Implement a program that allows the user to add new students to a database. Each student should have a unique ID, name, age, and grade.
# Allow the user to display the list of students.
# Implement a function to save the student database to a file.
# Add a menu system to navigate these options.


stud=[]        # initializing empty list           
while True:        # apply loop
    while True:        # apply loop for checking choice
        option=input("Enter your choice 'add','display','save' 'end' :").lower() #taking input
        if option=="add" or option=="display" or option=="save" or option=="end":  # checking conditions
            break               # breaking from loop if condition met
        else:
            print("please enter correct option")    
    if option=="add":                    # checking for choices               
          name=input("Enter Student name:")
          age=input("Enter Student age:")
          grade=input("Enter Student grade:")
          details={"name":name,"age":age,"grade":grade}         # making dictionary and append values in dictionary
          stud.append(details)                        # appending dictionary in list
          for i,student in enumerate (stud):      # displaying resullt
            print(f"Student {i}:")
            for key,value in student.items():
                  print(f"{key}:{value}")          
            print()
    elif option=="display":
          if not stud:                 # if no data in list
              print("No data Entered")
          else:
             for i,student in enumerate (stud):
               print(f"Student {i} : ")
               for key,value in student.items():
                    print(f"{key}:{value}")
               print()
    elif option=="save":
         if not stud:
             print("No data to save")
         else:
           user_file=input("Enter File Name to save:")   # taking filename input by user
           with open(user_file,"a+") as file:       # opening file in a+
             for i in stud:
               for key,value in i.items():
                   z=(f'{key}:{value}\n')
                   file.write(z)           # writting  content a file 
           file=open(user_file)        # again opening file
           file.seek(0)            # seek for moving cursor to start
           for i in file.readlines():       # read file line by line
             print(i)             # printing file
    elif option=="end":
        if not stud:                 # if not data
             print("No data entered ")
        else:
           for i,student in enumerate (stud):        # printing data
             print(f"student {i}")
             for key,value in student.items():
                print(f"{key}:{value}")                
             print()
        break     # breaking out of loop



