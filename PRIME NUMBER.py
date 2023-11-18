# Task:
# Write a Python program that takes an integer input from the user and prints whether it is a prime number or not. Use a for loop to check for divisibility.

# TAKING INPUT:
num=int(input("Enter An Integer:"))
# Initializing the count==0:
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
# Checking That number is prime or not:1
if count==2:
            print(f"{num} is the 'PRIME NUMBER'")

else:
    print(f"{num} is not a 'PRIME NUMBER'")


        
              

