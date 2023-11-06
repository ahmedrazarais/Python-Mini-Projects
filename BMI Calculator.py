# BMI CALCULATOR:
# taking input by user of thier weight:
mass=int(input("Enter your weight:"))
# conditions:
# weight from 1-40:underweight
# weight from 41-75:Normalweight
# weight from 76 -200:overweight
if mass<=40:
    print("You are Underweight\nTake Proper Deit")
elif 75>=mass>=41:
    print("You have Normal Weight\Just keep mantaining it") 
elif mass<=200:
    print("You have Over Weight\Take care of yourself Reduce your weight:")           
else: 
    print()    
