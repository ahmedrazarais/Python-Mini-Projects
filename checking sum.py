 
# Certainly! Here's another task:
# Write a Python program that asks the user to enter three numbers. The program should then check and print whether the sum of the three numbers is greater than, equal to, or less than 100.
# TAKING INPUT:
# INITIALIZING EMPTY LIST:
value=[]
for i in range(1,4):
    num=int(input(f"Enter {i} # Number:"))
    # TRANSFERING ALL INPTS TO LIST:
    value.append(num)
# CALCULATING SUM:
sum=sum(value)       
#CHECKING IF SUM IS GREATER THAN 100 OR NOT:
if sum>100:
    print(f"{sum} is greater than 100")
elif sum<100:
    print(f"{sum} is Lesser than 100") 
else:
    print(f"{sum} is Equal to 100")
     
