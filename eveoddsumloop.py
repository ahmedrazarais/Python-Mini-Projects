# # TAKING RANGE (1,100):
# Initializing sum to 0:
sum_odd=0
# INITIALIZING TOTAL TO 1 FOR PRODUCT:
total_odd=1
# MAKING A RANGE TO GET ALL ODD NUMBERS AND APPLYING FOR LOOP:
for i in range(1,100,2):
    sum_odd+=i
    total_odd*=i    
print(f"The Sum Of All Odd Numbers Between 1 to 100 is  {sum_odd}")    
print(f"The Product Of All Odd Numbers Between 1 to 100 is  {total_odd}")    

# INITIALIZUNG SUM TO ZERO:
sum_even=0
# INITIALIZING TOTAL TO one:
total_even=1
# Making a range for even numbers and applying for loop:
for i in range(2,101,2):
    sum_even+=i
    total_even*=i
print(f"The Sum Of All even Numbers Between 1 to 100 is  {sum_even}")    
print(f"The Product Of even  Numbers Between 1 to 100 is  {total_even}")     
    