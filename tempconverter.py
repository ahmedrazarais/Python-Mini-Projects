print("Temperature converter")
print("Enter 1 to convert Celsius To Fahrenheit")
print("Enter 2 to convert Fahrenheit To Celsius")
choice = int(input("Enter Your Choice 1-2: "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The Temperature In Fahrenheit is: {fahrenheit}")

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"The Temperature in Celsius is: {celsius}")

else:
    print("Invalid choice. Please enter 1 or 2.")
