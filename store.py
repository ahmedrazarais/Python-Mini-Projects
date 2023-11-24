
# Sure, here is a task that you can practice loops, if-else statements, and data types, without using functions:

# Task: Develop a simple program that simulates a vending machine. The vending machine should have three items available for purchase:

# Soda: $1.50
# Chips: $1.00
# Candy: $0.75
# The program should prompt the user to select an item and enter the amount of money they want to insert. The program should then check if the user has inserted enough money to purchase the item. If so, it should display a message indicating that the purchase was successful and dispense the item. If not, it should display a message indicating that the user needs to insert more money.


print("WELCOME TO THE ONLINE STORE!")
print()

user_choice = input("Do you want to sign up (yes/no):")

if user_choice.lower() == "yes":
    name = input("Enter your full name: ")

    while True:
        password = input("Enter your four-digit password: ")

        if 1000 <= int(password) <= 9999:
            break
        else:
            print("Please enter a valid four-digit password.")

    print(f"Congratulations {name}, you have successfully signed up!")

    while True:
        # Display menu options
        print("Here are the choices you can buy:")
        print("1. Soda")
        print("2. Juices")
        print("3. Colddrinks")
        print("4. Exit the app")

        # Get user's choice
        choice = input("Enter your choice: ")

        # Handle user's choice
        if choice == "1":
            print("Item soda added to your cart.")
            print(f"{name}, the total amount you have to pay is 2200.")
            payment_method = input("Enter payment method (cash or credit card): ")

            if payment_method.lower() in ["cash", "credit card"]:
                print(f"Thank you for your payment.")
            else:
                print("Invalid payment method. Please enter 'cash' or 'credit card'.")

        elif choice == "2":
            print(f"{name}, item juices added to your cart.")
            print(f"{name}, the total amount you have to pay is 5500.")
            payment_method = input("Enter payment method (cash or credit card): ")

            if payment_method.lower() in ["cash", "credit card"]:
                print(f"Thank you for your payment.")
            else:
                print("Invalid payment method. Please enter 'cash' or 'credit card'.")

        elif choice == "3":
            print(f"{name}, item colddrinks added to your cart.")
            print(f"{name}, the total amount you have to pay is 8000.")
            payment_method = input("Enter payment method (cash or credit card): ")

            if payment_method.lower() in ["cash", "credit card"]:
                print(f"Thank you for your payment.")
            else:
                print("Invalid payment method. Please enter 'cash' or 'credit card'.")

        elif choice == "4":

            print(f"{name}, hope you enjoyed shopping!")
            print(f"Have a nice day {name}")
            break

        else:
            print("Please enter a valid choice.")

elif user_choice.lower() == "no":
    # Since the user chose not to sign up,

    while True:
        # Display menu options
        print("Here are the choices you can buy:")
        print("1. Soda")
        print("2. Juices")
        print("3. Colddrinks")
        print("4. Exit the app")

        # Get user's choice
        choice = input("Enter your choice: ")

        # Handle user's choice
        if choice == "1":
            print("Item soda added to your cart.")
            print(f"Please enter your full name to proceed with checkout: ")
            name = input("Enter your full name: ")
            print(f"{name}, the total amount you have to pay is 2200.")
            payment_method = input("Enter payment method (cash or credit card): ")

            if payment_method.lower() in ["cash", "credit card"]:
                print(f"Thank you for your payment.")
            else:
                print("Invalid payment method. Please enter 'cash' or 'credit card'.")

        elif choice == "2":
            print(f"Item juices added to your cart.")
            print(f"Please enter your full name to proceed with checkout: ")
            name = input("Enter your full name: ")
            print(f"{name}, the total amount you have to pay is 5500.")
            payment_method = input("Enter payment method (cash or credit card): ")

            if payment_method.lower() in ["cash", "credit card"]:
                print(f"Thank you for your payment.")
            else:
                 print("Invalid payment method. Please enter 'cash' or 'credit card'.")   
        elif choice == "3":
             print(f"Item colddrinks added to your cart.")
             print(f"Please enter your full name to proceed with checkout: ")
             name = input("Enter your full name: ")
             print(f"{name}, the total amount you have to pay is 5500.")
             payment_method = input("Enter payment method (cash or credit card):")      
                
             if payment_method.lower() in ["cash", "credit card"]:
                print(f"Thank you for your payment.")    
             else:
                 print("Invalid payment method. Please enter 'cash' or 'credit card'.")   
        elif choice == "4":
            print(f"{name}, hope you enjoyed shopping!")
            print(f"Have a nice day {name}")
            break        




          
                
                     


               
                


                
             


   
        
    

        






