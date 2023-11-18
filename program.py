# 11. Write a Python program that allows the user to enter exactly twenty floating-point values. The program then prints the
# sum, average (arithmetic mean), maximum, and minimum of the values entered.

float_values=[]
for i in range(1,6):
    value=float(input(f"Enter {i} {"#"}  Float value:"))
    float_values.append(value)
print(f"You Entered These Values: {float_values}")    
# TAKING SUM:
total_sum=sum(float_values)
max_value=max(float_values)
min_value=min(float_values)
average=total_sum/i
print(f"THE TOTAL SUM IS: {total_sum}")     
print(f"THE MAX VALUE IS: {max_value}")     
print(f"THE MIN VALUE IS: {min_value}")     
print(f"THE AVERAGE IS: {average}")     