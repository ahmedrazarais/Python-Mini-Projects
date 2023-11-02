# Calculator
# Taking Input
num1=int(input("Enter Your First Number:"))
num2=int(input("Enter Your Second Number:"))
# providing choices to user
print("Press 1 For Addition:")
print("Press 2 For Subtraction:")
print("Press 3 For Multiplication:")
print("Press 4 For Division:")
print("Press 5 For Percentage:")
choice=int(input("Enter Your Choice FROM 1-5:"))
# conditions
if choice==1:
    print("The Sum Of Two Number Is :",num1+num2)
if choice==2:
    print("The Difference OF Twwo Number is :",num1-num2)
if choice==3:
    print("The Product Of Two Number is",num1*num2)
if choice==4:
    print("The Divisin Of Two Number is :",num1/num2)
if choice==5:
    print("The Percentage Of TwO Number is :",num1%num2)
# if user put invalid entry
else:
    print()

    

