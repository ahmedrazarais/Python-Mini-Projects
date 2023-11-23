# # # Developing the program to perform two simple transactions in a bank as long as user enters ,,u to continue
# # print("Enter Your Id It must in Four Digit Format (E.g: 1234 or 2345...) ")
# # # TAKING Input Of user Id:
                                                                
print("Enter Your Id It must in Four Digit Format (E.g: 1234 or 2345...) ")

# TAKING Input Of user Id:

while True:
    user_id = int(input("Enter Your Four Digit Id:"))
    if 1000 < user_id < 9999:
        break
    else:
        print("Please Enter Correct Id For Further Process")

# PRINTING RESULTS AFTER TAKING ID OF USER:

print("    MAIN MENU     ")
print("        *********    ")
print("Here are options that you can perform")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Login as Different User")
print("4. To Exit The Program")
print(" (Select Your Choice...)")
print()

# # CHECKING CHOICES ENTER BY USERS:
while True:
    while True:
        choice = int(input("Enter your Choice :"))
        if choice == 1 or choice == 2 or choice == 3 or choice==4:
            break
        else:
            print("Please Select Correct Choice")

    if choice == 1:
        amount_1 = input("How Much Money You Want To Deposit?__")
        print(f"The amount You Deposited is {amount_1}")

        while True:
            check = input("Do You Want To Continue? Press [Y,N]:_")
            if check in "YNyn":
                if check == "Y":
                    break
                else:
                    # Redirect to main menu if user enters y,n
                    print("Returning to main menu...")
                    break

        # Display "Hi, enter your choice again" after handling 'Y' or 'N'
        print("Hi, enter your choice again")

    elif choice == 2:
        amount_2 = input("How Much Money You Want To Withdraw?__")
        print(f"The amount You Withdraw is {amount_2}")

        while True:
            check = input("Do You Want To Continue? Press [Y,N]:_")
            if check in "YNyn":
                if check == "Y":
                    break
                else:
                    # Redirect to main menu if user enters 'N'
                    print("Returning to main menu...")
                    break

        # Display "Hi, enter your choice again" after handling 'Y' or 'N'
        print("Hi, enter your choice again")

    elif choice == 3:
        print("Now you can login as different User:")

        while True:
            user_id = int(input("Enter Your Four Digit Id:"))
            if 1000 < user_id < 9999:
                break
            else:
                print("Please Enter Correct Id For Further Process")                                                        
    elif choice==4:
        print("Thanks For Using Our Bank Sevices")   
        break     