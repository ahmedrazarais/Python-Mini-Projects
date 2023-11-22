# 15. Implement a program that requests four numbers (integer or floating-point) from the user. Your program should
# compute the average of the first three numbers and compare the average to the fourth number. If they are equal, your
# program should print 'Equal' on the screen.
# Test Data:
# Enter number 1: 4.5
# Enter number 2: 3
# Enter number 2: 3
# Enter last number: 3.5
# Expected Output: Equal

# APPLYING LOOP FOR TAKING INPUT:
while True:
        num1=float(input("Enter First number:")) 
        num2=float(input("Enter second number:")) 
        num3=float(input("Enter third number:")) 
        num4=float(input("Enter last number:")) 

        # finding average of first three numbers:
        avg123=(num1+num2+num3)/3
        # APPLYING CONDITIONS:
        if avg123==num4:
                print("Equal")
        else:
                print("not equal") 
        break      

    
