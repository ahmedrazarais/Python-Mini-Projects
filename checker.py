#    7. Write a Python program to check if a character entered by the user is an alphabet or a digit or a special character. If
# the user enters more than one character as input, the program prints some appropriate error message and exit.

# Taking input bu user:
value=(input("Enter the character:"))
# Checking the length:
if len(value)!=1:
    print("Enter Only One Character")

elif value. isalpha():
    print(f" It is an alphabet :{value}")    
elif value. isdigit():
    print(f" It is a digit: {value}")
elif  not value. isalnum(): 
    print(f"It is a character: {value}" ) 
else:
    print("It is something else")     