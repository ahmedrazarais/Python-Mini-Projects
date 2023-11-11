# 11. Write a Python program to check whether the triangle is equilateral, isosceles or scalene triangle. In equilateral
# triangle all three sides are equal, in isosceles triangle any two sides are equal, and in scalene triangle none of the three
# are equal. 
# TAKING INPUT BY USER OF SIDES OF TRIANGLE:
side1=float(input("Enter First Side:")) 
side2=float(input("Enter second Side:")) 
side3=float(input("Enter third Side:")) 
# FOR CHECKING EQUILTERAL TRIANGLE:
if side1==side2 and side1==side3:
    print("It is an equilteral triangle")
#FOR CHECKING ISOCELES TRIANGLE: 
elif side1==side2 or side1==side3 or side2==side3:
    print("It Is the Isoceles Triangle")    
# FOR CHECKING SCALENE TRIANGLE:
elif side1!=side2 or side1!=side3:
    print("It is the Scalene Triangle")    
else:
    print() 