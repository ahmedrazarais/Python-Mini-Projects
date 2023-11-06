# Making a program that calculates price of movie ticet on some conditions:
# Giving Information To User:
print("Hello Everyone!There is the new movie in the Thetre\nDon't Miss the opportunity Hurry Up! Grab the opportunity") 

# Taking input by user:
name=input("Enter Your Name:")
age=int(input("Enter your age:"))
print(f"Good Morning {name}")
# Giving Information about Discounts:
print("Price of ticket are different\n1. For students 5% Discount\n2. For Employees 2% discount\n3. For Housewife 3% discounts")
print("We have many discounts for you!")
print("Enter 1 if you are student!")
print("Enter 2 if you are emloyee!")
print("Enter 3 if you are housewife!")
# Providing choices to user:
choice=int(input("Enter Your Choice from 1-3:"))
# variable=price,discount1,discount2,discount3 
price=2000
# Conditions for students:
if choice==1:
    print("The official price of Ticket is 2000")
    discount1=(price * 5)/100
    print(f"Just because you are student we give 5 % discount to you\nNow the price of ticket is :{discount1}")
# conditions for emloyes: 
elif choice==2:
     print("The official price of Ticket is 2000")
     discount2=(price * 2)/100
     print(f"Just because you are Employee we give 2% discount to you\nNow the price of ticket is :{discount2}")
# conditions for housewife:  
elif choice==3:
     print("The official price of Ticket is 2000")
     discount3=(price * 3)/100
     print(f"Just because you are HouseWife we give 3% discount to you\nNow the price of ticket is :{discount3}")     
# conditions for someone else:  
else:
     result=(price* 1)/100
     print(f"We give you only 1% discount\nNow the price is :{result}")     

  
      
    


