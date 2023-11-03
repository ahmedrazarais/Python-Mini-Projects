# Taking input by user of max 6 digits:
print("Enter Integer of Maximum 6 Digits")
num1=int(input("Enter first integer:"))
num2=int(input("Enter second integer:"))
if len("num1")<=6 and len("num2")<=6:
    print(f"   {num1}\n{num2}")
else:
    print("lenth exceed limit")    
    
