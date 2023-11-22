# 12. Write code to find average of five non-negative integers entered by the user and print average
# Initializing total to zero:
total=0
# TAKING INPUT:
for i in range(5):
    num=int(input("Enter Non Negative Integer:"))
    # APPLYING CONDITION THAT USER SHOULD ENTER NONNEGATIVE INTEGER:
    while True:
        if num>0:
            break
        else:
            print("Please Enter Non Negative Integer")
            num=int(input("Enter Non Negative Integer:"))

    # CALCULATING THE SUM:    
    total+=num
# CALCULATING AVERAGE
avg=total/5
# PRINTING RESULTS:
print(f"The Total sum is : {total}")
print(f"The Total Average is : {avg}")

   