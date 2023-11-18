
obt_marks = 500
name = input("Enter your name:")
# MAKING AN EMPTY LIST:
subject = []
# initializing the list of subjects:
topics = ['Maths', 'Science', 'Physics', 'Chemistry', 'English']
# APPLYING LOOP FOR TAKING INPUT:
for topic in topics:
    marks = int(input(f"Enter your {topic} marks:"))
    # TRANSFER ALL MARKS TO SUBJECT LIST:
    subject.append(marks)
# CALCULATING PERCENTAGE:
# Initializing sum to zero:
sum = 0
for number in subject:
    sum += number
per = (sum / obt_marks) * 100
# FINDING MAXIMUM MARKS:
max_marks = max(subject)
max_marks_index = subject.index(max_marks)
max_subject = topics[max_marks_index]
# Finding minimum marks:
min_marks=min(subject)
min_marks_index=subject.index(min_marks)
min_subject=topics[min_marks_index]   
# PRINTING ALL RESULTS:
print(f"HEY {name} That is your Complete Result:")
print(f"{name} you got total marks = {sum}")
print(f"You got the maximum marks in {max_subject} and the score is {max_marks}")
print(f"You got the miminum marks in {min_subject} and the score is {min_marks}")
print(f"CONGRATULATIONS! {name} Percentage You got = {per}%")
# ASSIGNING GRADES:
if 100>=per>=88:
    print("You Achieved A Grade!")
elif  87>=per>=80:
    print("You Achieved A- Grade!")   
elif  79>=per>=75:
    print("You Achieved B+ Grade!")   
elif  74>=per>=70:
    print("You Achieved B Grade!")       
elif  69>=per>=67:
    print("You Achieved B- Grade!")       
elif  66>=per>=64:
    print("You Achieved C+ Grade!")       
elif  63>=per>=60:
    print("You Achieved C Grade!")       
elif  59>=per>=57:
    print("You Achieved C- Grade!")       
elif  56>=per>=54:
    print("You Achieved D+ Grade!")       
elif  53>=per>=50:
    print("You Achieved D Grade!")     
else:
    print("pass,You got no Grade") 
