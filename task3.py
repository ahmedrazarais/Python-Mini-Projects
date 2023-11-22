# 14. Repeat problem 12 adding an additional condition. If the user disobeys, the program prints some angry text and
# terminates.
total=0
count=0
while True:
    val=int(input("Enter Non Negative Integer:"))
    if val<0:
        print("I Think You Don't read the instruction carefully!")
        break
    total+=val
    count+=1
if count>1:
    avg=total/count
    print(f"The Total sum is : {total}")
    print(f"The Total Average is :{avg}")
else:
    print("Thanks Program Is Finished")
        