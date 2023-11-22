# 12. Write a Python program that allows the user to enter any number of nonnegative floating-point values. The user
# terminates the input list with any negative value. The program then prints the sum, average (arithmetic mean),
# maximum, and minimum of the values entered. The terminating negative value is not used in the computations.
# INITIALIZING TOTAL AND COUNT=0
total=0
count=0
# MAKING EMPTY LIST
values=[]
# APPLYING INFINITE LOOP FOR TAKING INPUT:
while True:
    user_input=float(input("Enter a Non negative float value: "))
    # APPLY CONDITION IF IT ENTER ANY NEGATIVE VALUE
    if user_input<0:
        break
    # Calculating sum
    total+=user_input
    count+=1
    # Convert user iputs into list
    values.append(user_input)
# APPLY CONDITION TO PREVENT 0/0 ERROR    
if count>1:
    # CALCULATING AVERAGE
    avg=total/count
    # Printing results of sum and avg
    print(f"The total Sum is : {total}")
    print(f"The total average is : {avg}")
# CALULATING MAX AND MIN VALUE:    
max_value=max(values)    
min_value=min(values) 
# PRINTING MAX AND MIN RESULTS
print(f"The max value is : {max_value}")
print(f"The min value is : {min_value}") 
    

