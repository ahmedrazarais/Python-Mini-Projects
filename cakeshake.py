# 7	You have been asked to develop a small online application in Python for a bakery. The application facilitates customers to order online by selecting different items form the online application. The mode of payment is ‘Cash on delivery’. The application provides the following features:
# 	Displays a menu showing items by name, their prices and serving size. Each item has a number which can be used by the customer to select the item. 
# 	Asks the customer to enter choice number, the customer can order only one item. On selecting a valid choice number, the customer is asked to enter a quantity for the selected item. Corresponding bill is calculated and printed for the customer. 
# The interface of the application should look as follows:
# 	Test Run 1
# Welcome to CakeShake!!
# We offer the following savouries:
#      1. Cake (Price: Rs. 650/-, Net weight: 2lbs)
#      2. Cookie Jars (Price: Rs. 240/-, Quantity: 1 jar)
#      3. Sandwiches (Price: Rs. 100/-, Serves 1)

# Enter your choice number: 1
# How many cakes? 2
# Your total bill is Rs. 1300
# Your order will be delivered in 30 minutes!
# Thank you for visiting!!
# 	Test Run 2
# Welcome to CakeShake!!
# We offer the following savouries:
#      1. Cake (Price: Rs. 650/-, Net weight: 2lbs)
#      2. Cookie Jars (Price: Rs. 240/-, Quantity: 1 jar)
#      3. Sandwiches (Price: Rs. 100/-, Serves 1)

# Enter your choice number: 6
# The choice number you entered is not valid.
# Thank you for visiting!!

# PRINTING DETAILS TO USER

print('''Welcome to CakeShake!!
We offer the following savouries:
1. Cake (Price: Rs. 650/-, Net weight: 2lbs)
2. Cookie Jars (Price: Rs. 240/-, Quantity: 1 jar)
3. Sandwiches (Price: Rs. 100/-, Serves 1)''')
# initailizing prices to variables
cake=650
cookie=240
sandwiches=100
# Taking input of users choice:
choice=int(input("Enter Your Choice Number:"))
# Checking conditions for choices
if choice==1:
    quantity=int(input("How many cakes?:"))
      # Calculatig bill
    bill=quantity*cake
      # PRinting bill
    print(f"Your Total Bill is {bill}")
    print("Your order will be delivered in 30 minutes!")
    print("Thank you for visiting!!")
elif choice==2:
        quantity=int(input("How many cookie jars?:"))
        # Calculatig bill
        bill=quantity*cookie
        # PRinting bill
        print(f"Your Total Bill is {bill}")
        print("Your order will be delivered in 30 minutes!")
        print("Thank you for visiting!!")
elif choice==3:
              quantity=int(input("How many cookie sandwiches?:"))
               # Calculatig bill
              bill=quantity*sandwiches
               # PRinting bill
              print(f"Your Total Bill is {bill}")
              print("Your order will be delivered in 30 minutes!")
              print("Thank you for visiting!!")
else:
        print("The Choice You entered is invalid!")              
        print("Thanks for visiting!")              
              


