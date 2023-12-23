
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



