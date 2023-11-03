# Taking input the value of radius by user for calculation of area and circumference of circle
rad=float(input("Enter value of radius:"))
PI=3.14
# calculating area and circumference:
area=PI*rad**2
circum=2*PI*rad
# printing result:
print(f"Area :{area}")
print(f"Circumference :{circum}")