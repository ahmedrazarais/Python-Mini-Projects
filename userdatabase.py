
# Task: User Database

# Create an empty dictionary called user_database.
# Implement a loop that allows users to add their information to the database. The information to be collected includes:
# User ID (an integer)
# User Name (a string)
# Age (an integer)
# Email (a string)
# Is Subscribed (a boolean)
# After collecting the information, store it as a dictionary for each user and add it to the user_database.
# Implement a loop that allows the user to search for a user by their ID.
# If the user is found, display their information. If not, print a message indicating that the user was not found.
# Save the user_database to a file, and load it from the file at the beginning of the program (if the file exists).
# This task should help you practice a variety of Python concepts. Feel free to customize it based on your current level of knowledge and add more complexity as needed. Good  -

print("\tUSER DATABASE")
print('''You Have 3 options To Do 
      1. Add the Data
      2. Search the Data
      3. Save the Data''')

final_list=[]         # MAKING AN EMPTY LIST TO TAKE USER INPUT
while True:            # APPLY OVERALL LOOP
    while True:         # APPLY LOOP TO TAKE USER CHOICE
     choice=input('Entere Your Choice add or search or save or end:').lower()
     if choice=="add" or choice=="search" or choice=="save" or choice=="end":
        break
     else:
        print("Please Enter Correct Choice")
    if choice=="add":            # CHECKING CONDITIONS NOW
       try:                      # USE TRY EXCEPT TO AVOID CRUSHING PROGRAM
        user_id=int(input("Enter Your Id in digits:")) 
        user_name=input("Enter Your Full Name:")
        age=int(input("Enter Your age in digits:"))
        email=input("Enter Your Email:") 

         # APPENDING ALL VALUES IN DICTIONARY
        user_database={"USERID":user_id,"AGE":age,"USERNAME":user_name,"EMAIL":email}
       
        #APPENDING DICTIONARY INTO LIST
        print()
        final_list.append(user_database)
        for i in final_list:         #PRINTING IN STANDARD FORM
          for key,value in i.items():
             print(f"{key}:{value}")
          print()
       except ValueError:
          print("Invalid input TRY AGAIN!!")

    elif choice=="search":        # CHECKING FOR SEARCH CONDITIONS
       if not final_list:         # IF LIST IS EMPTY
          print("There Is No Data To Display")
       else:                      # IF LIST IS NOT EMPTY
        fix="USERID"              #FIX ON USERID
        try:                      # USING TRY EXCEPT TO AVOID CONFLICT
          user_input_id=int(input("Enter Your ID to Search Your Record:"))
          found=False
          for check in final_list:
           if check.get(fix)==user_input_id:     # IF COND IS TRUE
              found=True         # MAKING FOUND TRUE
              if found:
                 print(f'Your Id Is :{check.get("USERID")}') 
                 print(f'Your Full Name Is :{check.get("USERNAME")}') 
                 print(f'Your age is :{check.get("AGE")}') 
                 print(f'Your email Is :{check.get("EMAIL")}') 
          if not found:
           print("You Entered Wrong Id Not match")   
        except ValueError:
          print("Id Must Be In Digits")

    elif choice=="save":
       if not final_list:
          print("Enter Some Data To Save In a File")
       else:
        #TAKING FILE NAME AS INPUT
        file_name=input("Enter The File Name:")
        with open(file_name,"a+") as file:
          for each in final_list:
             for key,value in each.items():
                file.write(f"{key}:{value}\n")     #WRITE DATA IN A FILE

        #ASKING THE USER TO SEE CONTENT OR NOT        
        user_ask=input("Did You Want To see contents of file yes or no ?:").lower()
        if user_ask=="yes":
         print("You Entered That Data")
         with open (file_name) as f:
          contents=f.read()
          print(contents)
        else:
          print("Alright Select your choice") 
     # breaking out of program if choice==end
    elif choice=="end":
      if not final_list:
        print("No Data Entered")
      else:
       print(f"Your Complete Data That You Entered Is:")
       for each in final_list:
         for key,value in each.items():
          print(f"{key}:{value}")
      break
    
    
    
    
    