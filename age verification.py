# Taking input by the user of thier age and then told them thier criteria for voting
name=(input("Enter Your Name:"))
print("Hello",name)
print("There is voting activity ,Now check i you are eligible or not")
age=int(input("Enter Your Age:"))
if 30>=age>=18:
    print("You are eligible to vote!")
if 60>=age>=31:  
    print("You are slightly old for voting this year ")    
elif age<15:
    print("You are so young")    
else:
    print()    