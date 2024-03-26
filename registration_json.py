import json

class Register:
    def __init__(self):     
        # set file path according to your working directory
        self.file_path="Python-Mini-Projects/register.json"
        self.account_list=[]


    def read_data_from_file(self):
        try:
            with open(self.file_path) as file:
                contents = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            contents = []  # Initialize with an empty list if file doesn't exist or is empty
        return contents


        
    
    def get_username(self):
        contents = self.read_data_from_file()
        while True:
            username = input("Enter Username (enter 0 to go back): ")
            if username == "0":
                print("Going to previous option...")
                return None  # Return None to indicate user wants to go back

            if len(username) > 1:
                username_found = any(check["username"] == username for check in contents)
                if username_found:
                    print("Sorry, this username is already taken. If this is your account, please login.")
                else:
                    print("Username set successfully.")
                    return username  # Return the username when it's valid
            else:
                print("Please enter a valid username or enter 0 to go back.")


        
    def get_password(self):
        print("Now proceed for password...\n")
        while True:
            password=input("Enter password enter 0 to back:")
            if password=="0":
                return
            if len(password)>1:
                return password
            else:
                print("Please enter valid password\n")
    
    def registration(self):
        username=self.get_username()
        if username:
            password=self.get_password()
            if password:
                accounts_dic={"username":username,"password":password}
                self.account_list.append(accounts_dic)
                with open(self.file_path,"w") as file:
                    json.dump(self.account_list,file)
                
                    print("Account created suceesfully")
                    return

       
                    
class Login(Register):
    def __init__(self):
        super().__init__()


    def get_username(self):
        contents=self.read_data_from_file()
        while True:
            username=input("Enter username for login enter 0 to back:")                           
            if username=="0":
                return

            username_found= any(check["username"]==username for check in contents)
            if username_found:
                print("Correct username.\n")
                return username
            else:
                print("Invalid username. Please enter correct username.\n")

    
    def get_password(self, username):
        contents = self.read_data_from_file()
        for account in contents:
            if account["username"] == username:
                while True:
                    password = input("Enter password for login, enter 0 to go back:")
                    if password == "0":
                        return

                    if password == account["password"]:
                        print("Correct credentials..\n")
                        print("Login successful...enter in market")
                        return password
                    else:
                        print("Invalid password. Please enter correct password.\n")
                
        else:
            print("Username not found.")

    
    def login_process(self):
        username=self.get_username()
        if username:
            password=self.get_password(username)
            if password:
                print("Welcome to raba store.\n")
        
        
                
            
register=Register()
login=Login()

while True:
    print("1.Register.")
    print("2.Login.")
    print("3.exit.\n")

    choice=input("Enter your choice:")
    if choice=="1":
        register.registration()
    elif choice=="2":
        login.login_process()
    elif choice=="3":
        break
    else:
        print("Invalid choice.\n")

    
    