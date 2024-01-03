final=[]
file_name=input("Enter FIle Name:")# only for us after we set our file
def first_name():
    while True:
     first_name = input("Enter Your First Name:")
     new_name=[char for char in first_name if char.strip()]
     if len(new_name)>2: 
        break
     else:
        print("First Name should have Atleast Three Words")
        print("Enter Again")

def last_name():  
    while True:
        last_name = input("Enter Your Last Name:") 
        new_name=[char for char in last_name if char.strip()]
        if len(new_name)>2:  
            break
        else:
            print("Last Name should have Atlesat Three Words")
            print("Enter Again")
        

def address():
    while True:
     address = input("Enter Your address:")
     new_address=[char for char in address if char.strip()]
     if len(new_address)>2:
        break
     else:
        print("Address should have Atlesat Three Words")
        print("Enter Again")
      
def signup(final):
   with open(file_name) as file:
      x="@#$!"
      final=[]
      for line in file:
         data=line.strip().split(f"{x}")                     
         user_dic={"username":data[0],"password":data[1],"passwordhint":data[2]}
         final.append(user_dic)

   while True:
      user_name = input("Enter User Name Don't Contain Spaces : ")
      if " " not in user_name and len(user_name)>1:
         for check in final:
               if user_name==check["username"]:
                     print('User Name Is Already Taken')
                     print('Please Select Another Username')
                     print('If You Already Have An Account Please Login!')
                     return                                       
         while True:
                password=input("Enter Your Password:")                  
                if any(char.isdigit() for char in password) and  any(not (char.isalnum()) for char in password) and len(password)>=8:

                   while True:
                    password_hint = input("Enter Password Hint:")
                    with open(file_name, "a+") as file:
                      file.write(f"{user_name}{x}{password}{x}{password_hint}\n")
                      file.seek(0)

                      print("Signup Successfully")
                      return                            
                else:
                     print("Password Must Contains Atleast 8 characters\nAtleast 1 2 Digits With one or more special character")
                
      else:
         print("User Name Should Not Contain Spaces")
         print("It Is mandatory To Fill This Field")
        
# signup(final)


def login(final):
   user_name=input("Enter Your User Name:")
   x="@#$!"
   with open(file_name) as file:
    final=[]
    for line in file:
      data=line.strip().split(f"{x}")
      user_dic={"username":data[0],"password":data[1],"passwordhint":data[2]}
      final.append(user_dic)
   user_name_check=False
   for every in final:
      if user_name==every["username"]:
           user_name_check=True
           while True:
            password=input("Enter Your Password:")
            if password==every["password"]:
              print("Login Successfully")
              break
            else:
             print("Invalid Password")  
             print(f"Password Hint : {every["passwordhint"]}")
             user_ask=input("Did You Want To Continue yes or no?:").lower()
             if user_ask=="no":
                break
   if not user_name_check:
      print("Invalid Username")
# login(final)
      
def file_data_read(final):
    x = "@#$!"
    final.clear()  # Clear existing data before reading from file
    with open(file_name) as file:
        for line in file:
            data = line.strip().split(f"{x}")
            user_dic = {"username": data[0], "password": data[1], "passwordhint": data[2]}
            final.append(user_dic)


def delete_account(final):
    x="@#$!"
    user_name_to_delete = input("Enter User Name To Delete Record:").strip()

    with open(file_name, "r") as file:
        lines = file.readlines()

    new_lines = []  # Store modified lines here
    deleted = False  # Flag to track deletion
    for line in lines:
        data = line.strip().split(f"{x}")
        if data[0] != user_name_to_delete:
            new_lines.append(line)  # Keep lines for other usernames
        else:
            deleted = True
            print(f"Account for {user_name_to_delete} deleted successfully.")
    if not deleted:
       print("No Username Of That Name")
    with open(file_name, "w") as file:
        file.writelines(new_lines)  # Write back the modified lines

    # Update final list only if deletion occurred
    if deleted:
        final = [user for user in final if user["username"] != user_name_to_delete]
# delete_account(final)

def info_admin():
     print("1. Add Any Account")
     print("2. Search any  Account")
     print("3. See All Data")
     print("4. Delete any Account")
     print("5. Exit Out Of program")

def admin_login(final):
   x="@#$!"
   admin_user_name="drmaria"
   admin_psd="1234"
   user_username_input=input("Enter Admin User Name:")
   User_Password_input=input("Enter  Admin Password:")
   if user_username_input==admin_user_name and User_Password_input==admin_psd:
      print("\t\tWELCOME TO ADMIN PAGE")
      while True:
         info_admin()
         print()
         choice=input("Enter Your Desired Option:")
         if choice=="1":
            signup(final)
            file_data_read(final)  # Reload data after adding  
         elif choice=="2":         
            file_data_read(final)
            fix="username"
            user_name_Ask=input("Enter User Name To Search Record:")
            has_found=False
            for every in final:
               if every.get(fix)==user_name_Ask:
                  has_found=True
                  if has_found:
                    print(f'UserName: {every.get("username")}')
                    print(f'Password: {every.get("password")}')
                    print(f'PasswordHint: {every.get("passwordhint")}')
                    break
            if not has_found:
               print("No UserName Match In Record")
         elif choice=="3":
               file_data_read(final)
               print("\tUSERS DETAILS")
               print()
               print(f"{"UsersNames"}:{"Passwords"}")
               print()
               for dic in final:
                  for key,value in dic.items():
                     print(f"{key} : {value}")
                  print()
         elif choice=="4":
            delete_account(final)
         elif choice=="5":
            print("Program Is Exiting..")
            print()
            break
         else:
            print("Invalid Choice Please Select Valid Choice")
   else:
      print("Invalid UserName or Password")
# admin_login(final)
   
print("\t Welcome To Computer Gala")
print("1.Signup As User")
print("2.Login As User")
print("3.Login As Admin")
print("4.To Exit")
while True:
   choice=input("Enter Your Choice:")
   if choice=="1":
      print("Create Your Account")
      print()
      first_name()
      last_name()
      address()
      signup(final)
   elif choice=="2": 
      print("Now You Can Login..")
      print()
      login(final)
   elif choice=="3":
      admin_login(final)
   elif choice=="4":
      print("Program Is exiting")
      break
   else:
      print("Invalid Choice")





































































































# def signup(final):
#    with open(file_name) as file:
#       final=[]
#       for line in file:
#          data=line.strip().split()                     
#          user_dic={"username":data[0],"password":data[1],"passwordhint":data[2]}
#          final.append(user_dic)

#    while True:
#       user_name = input("Enter User Name Don't Contain Spaces : ")
#       if " " not in user_name and len(user_name)>1:
#          for check in final:
#                if user_name==check["username"]:
#                      print('User Name Is Already Taken')
#                      print('Please Select Another Username')
#                      print('If You Already Have An Account Please Login!')
#                      return                                       
#          while True:
#                 password=input("Enter Your Password:")
#                 if " " not in password :
                  
#                   if any(char.isdigit() for char in password) and  any(not (char.isalnum()) for char in password) and len(password)>=8:


#                    while True:
#                     password_hint = input("Enter Password Hint:")
#                     if " " not in password_hint:
#                      with open(file_name, "a+") as file:
#                       file.write(f"{user_name} {password} {password_hint}\n")
#                       file.seek(0)

#                       print("Signup Successfully")
#                       return
#                     else:
#                        print("Password hint should not contain spaces. Please try again.")

                             
#                   else:
#                      print("Password Must Contains Atleast 8 characters\nAtleast 1 2 Digits With one or more special character")
#                 else:
#                    print("Password should not contain spaces ")
#                    print("It Is Mandatory To Fill This Field ")
#       else:
#          print("User Name Should Not Contain Spaces")
#          print("It Is mandatory To Fill This Field")


# signup()
























































# def login(final):
#    user_name=input("Enter Your User Name:")
#    with open(file_name) as file:
#     final=[]
#     for line in file:
#       data=line.strip().split()
#       user_dic={"username":data[0],"password":data[1],"passwordhint":data[2]}
#       final.append(user_dic)
#    user_name_check=False
#    for every in final:
#       if user_name==every["username"]:
#            user_name_check=True
#            while True:
#             password=input("Enter Your Password:")
#             if password==every["password"]:
#               print("Login Successfully")
#               break
#             else:
#              print("Invalid Password")  
#              print(f"Password Hint : {every["passwordhint"]}")
#              user_ask=input("Did You Want To Continue yes or no?:").lower()
#              if user_ask=="no":
#                 break
#    if not user_name_check:
#       print("Invalid Username")
# login(final)



















# final=[]
# file_name="C:/Users/ideal pc/Desktop/ComuterProgramming/ComputerProgramming/userdata.txt"
# with open(file_name) as file:
#    for line in file:
#       data=line.strip().split()
#       final.append({"username":data[0],"password":data[1]})
# def signup():
#    while True:
#       user_name = input("Enter User Name Don't Contain Spaces : ")
#       if " " not in user_name and len(user_name)>1:
#          for check in final:
#                if user_name==check["username"]:
#                      print('User Name Is Already Taken')
#                      return                                       
#          while True:
#                 password=input("Enter Your Password:")
#                 if " " not in password :
                  
#                   if any(char.isdigit() for char in password) and  any(not (char.isalnum()) for char in password) and len(password)>=8:
                
        
#                    with open(file_name,"a+") as file:
#                     file.write(f"{user_name} {password}\n")
#                     file.seek(0)

#                     for line in file:
#                      data=line.strip().split()                     
#                      user_dic={"username":data[0],"password":data[1]}
#                      final.append(user_dic)
#                    print("Signup Successfully") 
#                    return  
                
#                   else:
#                      print("Password Must Contains Atleast 8 characters\nAtleast 1 2 Digits With one or more special character")
#                 else:
#                    print("Password should not contain spaces")
   








# final=[]
# file_name="C:/Users/ideal pc/Desktop/ComuterProgramming/ComputerProgramming/userdata.txt"
# with open(file_name) as file:
#    for line in file:
#       data=line.strip().split()
#       final.append({"username":data[0],"password":data[1]})

# def signup(final):
#    while True:
#       user_name = input("Enter User Name Don't Contain Spaces : ")
#       if " " not in user_name and len(user_name)>1:
#          for check in final:
#                if user_name==check["username"]:
#                      print('User Name Is Already Taken')
#                      return                                       
#          while True:
#                 password=input("Enter Your Password:")
#                 if " " not in password :
                  
#                   if any(char.isdigit() for char in password) and  any(not (char.isalnum()) for char in password) and len(password)>=8:
                  
        
#                      with open(file_name,"a+") as file:
#                       file.write(f"{user_name} {password}\n")
#                       file.seek(0)

#                       for line in file:
#                        data=line.strip().split()                     
#                        user_dic={"username":data[0],"password":data[1]}
#                        final.append(user_dic)
#                      print("Signup Successfully") 
#                      return  
                  
          
#                   else:
#                      print("Password Must Contains Atleast 8 characters\nAtleast 1 2 Digits With one or more special character")
#                 else:
#                    print("Password should not contain spaces ")
#                    print("It Is Mandatory To Fill THis Field ")
#       else:
#          print("User Name Should Not Contain Spaces")
#          print("It Is mandatory To Fill This Field")