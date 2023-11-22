# 15. Implement a program that requests four numbers (integer or floating-point) from the user. Your program should
# compute the average of the first three numbers and compare the average to the fourth number. If they are equal, your
# program should print 'Equal' on the screen.
# Test Data:
# enter number=1234
# avg of first three number==last num print(equal)


# APPLYING LOOP FOR TAKING INPUT:
while True:
    num=int(input("Enter Four Digit Number:"))
    # checking that number should be 4 digit:
    if  1000<num<9999:
        break
    else:
        print("Please Enter Appropite Four Digit Number:")
# extracting digits:
thousands_digits=(num//1000)
hundred_digits=(num%1000)//100
tens_digits=(num%100)//10
units_digits=(num%10)

# finding average of first three:
avg=(thousands_digits+hundred_digits+tens_digits)/3

# APPLYING CONDITIONS FOR CHECKING AVG ==LAST NUM:
if avg==units_digits:
    print("EQUAL!")
else:
    print("Not equal !")    