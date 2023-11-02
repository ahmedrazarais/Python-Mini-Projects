# Tking input by user for a,b,c:
a=int(input("Enter your First number: "))
b=int(input("Enter your Second number: "))
c=int(input("Enter your Third number: "))
# Apply formula:
X1=(-b - ((b**2-4*a*c) ** 0.5)) / (2 * a)
X2=(-b + ((b**2-4*a*c) ** 0.5)) / (2 * a)
# printing result::
print("The value of x1:",X1)
print("The value of x2:",X2)