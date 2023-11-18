# Certainly! Here's another task:
# # Write a Python program that takes two numbers as input from the user. Check if the first number is divisible by the second number. Print a message indicating whether the first number is divisible by the second or not using if-else statements.

# TAKING INPUT BY USER:
num_1=int(input('Enter The first Integer:'))
num_2=int(input('Enter The second Integer:'))
# CHECKING THAT NUM1 IS DIVISIBLE BY NUM2:
if num_1%num_2==0:
    print(f"The number {num_1} is completely divisble by {num_2}")
else:
    print(f"The number {num_1} is not completely divisble by {num_2}")
