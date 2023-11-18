# Positive Product of List Elements:
# Create a program that takes a list of integers as input and checks if the product of all positive numbers is positive.

# TAIKNG INPUT BY USER:
value_list=[]
for i in range(1,6):
    value=int(input(f"Enter {i} # Integer Value:"))
    value_list.append(value)
# Finding product of list:   
total=1
for number in value_list:
        total*=number
# CHECKING IF PRODUCT IS POSITIVE OR NEGATIVE        
if total>0:   
              print(f"The product of all nummbers is : {total}")
else:
              print(f'PRODUCT IS NEGATIVE: {total}')


