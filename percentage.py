# 2. Write a Python program to input marks (obtained marks as well as maximum marks) for five subjects Physics,
# Chemistry, Biology, Mathematics and Computer. It calculates and prints percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

# TAKING INPUT BY USER PF OBTAINED AND TOTAL MARKS:
tot_marks=500
obt_marks1=int(input("Enter obtained Marks in physics (Out of 100):"))
obt_marks2=int(input("Enter obtained Marks in chemistry (Out of 100):"))
obt_marks3=int(input("Enter obtained Marks in Biology (Out of 100):"))
obt_marks4=int(input("Enter obtained Marks in Mathematics (Out of 100):"))
obt_marks5=int(input("Enter obtained Marks in Computer (Out of 100):"))
# calculating percentages:
per=(obt_marks1+obt_marks2+obt_marks3+obt_marks4+obt_marks5)/tot_marks
percentage=per*100
# PRINTING PERCENTAGE:
print(f"Congrats you got: {percentage}")
# ASSIGNING GRADES:
if percentage>=90:
    print("GradeA")
elif percentage>=80:
    print("Grade B")
elif percentage>=80:
    print("Grade C")    
elif percentage>=70:
    print("Grade D")
elif percentage>=60:
    print("Grade E")
elif percentage>=40:
    print("Grade F")
else:
    print("Fail")