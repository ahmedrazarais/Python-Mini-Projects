#making a bank class

#initial the class
class Bank_system:
    def __init__(self):
        self.pin=0
        self.balance=0
        self.depositmoney=0
        self.withdrawamount=0


    def set_Pin(self):
        print("Welcome Sir Now You can set your pin..")
        print()
        while True:
            try:
                pin=input("Enter Your Four Digit Pin:")
                if len(pin)==4 and pin.isdigit():
                    pin=int(pin)
                    print("Congratulation pin set succesfully..")
                    print()
                    print(f"Now you can use this pin {pin} for further use.")
                    print()
                    self.pin=pin
                    return self.pin
                else:
                    print("Pin must contain 4 digits.")
                    print()
            except ValueError:
                print("Please Enter in Digits.")
                print()



    def check_pin(self):
    # Check if PIN is not set
        if self.pin == 0:
            print("Sorry, you can't access the system until you set a PIN.")
            print()
        else:
            # Keep prompting for PIN until a correct one is entered or user decides to go back
            while True:
                pin = input("Enter Your Four Digit Pin (enter 0 to go back): ")
                # If user decides to go back
                if pin == '0':
                    return

                # Check if entered PIN matches the stored PIN
                if pin == str(self.pin):  # Convert pin to string for comparison
                    return "found"  # Return "found" if PIN is found

                # If PIN is incorrect, prompt again
                print("Incorrect PIN. Please try again.")




    def deposit_money(self):
        check=self.check_pin()
        if check:
            print("Welcome!Now you can deposit money.")
            print()
            while True:
                try:
                   money=int(input("Enter how much you want to deposit?:"))
                   if money>0:
                       print(f"Congratulations Total {money} amount deposited to your account.")
                       self.depositmoney+=money
                       self.balance+=money
                       return
                    
                   else:
                       print("Please Enter non-negative number")


                except ValueError:
                    print("Please Enter valid digit.")
                    print()

    
    def withdraw_money(self):
        check=self.check_pin()
        if check:
            if self.balance!=0:
                print("Welcome!Now you can withdraw money.")
                print()
                while True:
                    try:
                        money_withdraw=int(input("Enter Amount You want to withdraw (enter 0 to back):"))
                        if money_withdraw==0:
                            print("Going to previous section..")
                            return
                        # checking balance must be graeter than withdraw amount.
                        if money_withdraw>0 and money_withdraw<=self.balance:
                            print()
                            print(f"Amount {money_withdraw} PKR withdraw successfully.")
                            self.balance-=money_withdraw
                            self.withdrawamount+=money_withdraw
                            print()
                            print(f"Now total balnce of your account is :{self.balance}")
                            print()
                            return

                        else:
                            print(f"sorry,you cant withdraw that amount {money_withdraw}PKR")
                            print()
                            print(f"Your account balance is {self.balance}")
                
                    except ValueError:
                        print("Please Enter In digts.")
                        print()
            else:
                print("sorry your account balance is null you cant withdraw amount.")
                print()
                return
                

    # function to show account details
    def view_account_details(self):
        check=self.check_pin()          
        if check:
            print("\t\tAccounts Details")
            print()
            print(f"\tAccount Pin: {self.pin}")
            print(f"\tAccount Balance: {self.balance} PKR")
            print(f"\tAmount Deposited: {self.depositmoney} PKR")
            print(f"\tAmount Withdraw :{self.withdrawamount} PKR")
            print()
            print()

    

    def main_system(self):
        print("\t\tWelcome To bank Management system.")
        while True:

            print("\t1.View your account details")
            print("\t2.Set Pin of account.")
            print("\t3.Deposit money in account")
            print("\t4.Withdraw money from account")
            print("\t5.Exit from system.")
            print()
            choice=input("Enter your Choice in system:").strip()
            if choice=="1":
                self.view_account_details()
            
            elif choice=="2":
                self.set_Pin()

            elif choice=="3":
                self.deposit_money()

            elif choice=="4":
                self.withdraw_money()

            elif choice=="5":
                print("System is ending...")
                print()
                return
            else:
                print("Invalid Choice Please Select From Given Choice.")
                print()


           

bankarena=Bank_system()
bankarena.main_system()
        
          

                        


