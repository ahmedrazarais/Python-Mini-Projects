
# Question 3 
# Develop a program to calculate and print result for a student as follows.
# 3.a Input name of the course, obtained marks and maximum/total marks from the user. Store this information in a 4 dictionary as follows:
# (course name: [obtmarks,totmarks ]}
# The user should be able to enter data for as many courses as he/she wants, enters 0 as course name to terminate.
# 3.b Develop a function called grade which inputs a value for percentage marks and returns the grade as per the 4 following criteria:
# Percentage >90% : Grade A
# Percentage >= 80% : Grade B Percentage >= 70% : Grade C Percentage >= 60% : Grade D Percentage 60% : Grade F
# 3.c Write code to traverse the dictionary formed in question 3.a, and calculate percentage score and grade for each 4 course. Use the function grade developed in question 3.b to find the grade value. For each course, print the calculated percentage and grade along with the course name on console.




users_person = {}  # MAKING AN EMPTY DICTIONARY
while True:  # APPLYING LOOP FOR TAKING INPUT
    course_name = input("Enter Course Name:")
    if course_name == "0":  # BREAK ON CERTAIN CONDITION
        break
    else:
        while True:
            try:  # USE TRY EXCEPT TO AVOID CONFLICTS
                obt_marks = int(input("Enter Obtained Marks:"))
                if obt_marks > 0:  # Check if obtained marks are greater than zero
                    break
                else:
                    print("Obtained Marks must be greater than zero")
            except ValueError:
                print("Must be in digits")
        
        while True:
            try:
                tot_marks = int(input("Enter Total Marks:"))
                if tot_marks > 0:  # Check if total marks are greater than zero
                    break
                else:
                    print("Total Marks must be greater than zero")
            except ValueError:
                print("Must be in digits")

        # Update Users Dictionary
        users_person.update({course_name: [obt_marks, tot_marks]})

# Making a function to return grade
def grade(percentage):
    if percentage > 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# Checking conditions for calculating grade and percentage
for course_name, marks in users_person.items():
    obt_marks, tot_marks = marks  # Unpack obtained marks and total marks
    if obt_marks > 0 and tot_marks > 0:  # Check if both obtained and total marks are greater than zero
        percentage = (obt_marks / tot_marks) * 100
        letter_grade = grade(percentage)
        print(f"{course_name}: Percentage: {percentage}%, Grade: {letter_grade}")
    else:
        print(f"{course_name}: Invalid marks - both obtained and total marks must be greater than zero")
