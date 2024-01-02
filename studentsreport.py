# Collect Data and Write to File:

# Ask the user to enter the number of students.
# For each student, prompt the user to enter the student's name and three exam scores.
# Write this information to a file.
print("\tSTUDENTS GRADE CALCULATION SYSTEM")
file_name=input("Enter File Name To Write Data In That File:")
with open(file_name,"w") as file:
     while True:
        try:
           stud_num=int(input("Enter Number Of Students To Enter Data:"))
           break
        except ValueError:
           print("Invalid Input Write In Digits")
     stud_list=[]
     for i in range(1,stud_num+1):
        stud_name=input(f"Enter {i} Student Name:")
        while True:
           try:
             sub_mark_1=float(input("Enter Student Marks of first subject:"))
             sub_mark_2=float(input("Enter Student Marks of second subject:"))
             sub_mark_3=float(input("Enter Student Marks of  third subject:"))
             break
           except ValueError:
              print("Invalid Input Write In Number")
        stud_dic={"Name":stud_name,"Subject1":sub_mark_1,"Subject2":sub_mark_2,"Subject3":sub_mark_3}
        stud_list.append(stud_dic)
     for check in stud_list:
        for key,value in check.items():
            file.write(f"{key} {value} ")
        file.write("\n")    
# Read Data from File and Calculate Grades:
# Read the student data from the file.
# Calculate the average score and determine the grade for each student.
# Print Summary Report
with open(file_name) as read_file:
        students_list=[]
        for line in read_file:
            data=line.strip().split()
            stud_dic={"Name":data[1],"Subject1":float(data[3]),"Subject2":float(data[5]),"Subject3":float(data[7])}
            students_list.append(stud_dic)
        for check in students_list:
           for key,value in check.items():
              print(f"{key}:{value}")
           print()
        print()
        fix_name="Name"
        fix_sub_1="Subject1"
        fix_sub_2="Subject2"
        fix_sub_3="Subject3"
        
# Grades Distribution
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
        print("Report Summary:")
        for check in students_list:
         total_marks = sum([check.get(fix_sub_1), check.get(fix_sub_2), check.get(fix_sub_3)])
         avg_marks = total_marks / 3

         print(f"{check.get(fix_name)} got total marks {total_marks} and average marks {avg_marks}")

         #APPLYING CONDITIONS FOR GRADE
         if 100 >= avg_marks >= 90:
          print(f"{check.get(fix_name)} Got A grade")
         elif 89 >= avg_marks >= 80:
          print(f"{check.get(fix_name)} Got B grade")
         elif 79 >= avg_marks >= 70:
          print(f"{check.get(fix_name)} Got C grade")
         elif 69 >= avg_marks >= 60:
          print(f"{check.get(fix_name)} Got D grade")
         elif avg_marks < 60:
          print(f"{check.get(fix_name)} Got F grade")



            
      

