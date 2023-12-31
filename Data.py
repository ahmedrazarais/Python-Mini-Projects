# Task: Data Analysis
# You have a file named  that contains information about employees in a company. Each line in the file represents a different employee and has the following format:

# File Handling:
# Open the  file and read its contents.
# Store the data in a suitable data structure to work with (e.g., list of dictionaries).

#Taking INPut of user file name:
print("\tDATA ANALYSIS PROGRAM")
file_name=input("Enter File Name with extension like (abc.txt) :")
new=[]
try:
   with open(file_name) as file:
    print("Data In a File is:")
    print()
    for line in file:
        data=line.strip().split(",")
        age=int(data[1])
        salary=int(data[3])            # converting file data into lists of dictionaries
        employe_dic={"Name":data[0],"Age":age,"Department":data[2],"Salary":salary}
        new.append(employe_dic)
    for each in new:
        for key,value in each.items():
            print(f"{key}:{value}")
        print()
    
# Calculate and print the average age of all employees.
    fix="Age"
    age_list=[]
    for each in new:
        if fix in each:
            z=each.get(fix)
            age_list.append(z)
    average_age=sum(age_list)/len(age_list)
    print(f"Age Of all Employees : {age_list}")
    print(f"Average Age Of Employees is : {average_age}")
    print()        
# Find and print the employee with the highest salary.

    fix="Salary"
    salary_lst=[]
    for dic in new:
        if fix in dic:
            sal=dic.get(fix)
            salary_lst.append(sal)
    maximum=max(salary_lst)

#Finding name of man of maximum salaray
    final=maximum
    fix="Name"
    for dic in new:
        if final in dic.values():
            employe_name=dic.get(fix)

    print(f"{employe_name} Has The Highest Salary That is {maximum} ")
    print()
            
# Create a dictionary where keys are department names and values are lists of employees in each department.


    new_dic={}
    department="Department"
    name="Name"
    for each in new:
        names=each.get(name)
        departments=each.get(department)
        new_dic.update({departments:names})
    for key,value in new_dic.items():
        print(f"{key} :{value}")
    print()
            
# Print the names of employees who are older than 30.  
    fix_name="Name"
    fix_age="Age"
    age=[]
    for each in new:
        if each.get(fix_age)>=30:
            name=each.get(fix_name)
            age.append(name)
    print("Employess Who are above or just 30 are :")
    for names in age:
        print(names)
    print()
     
# Increase the salary of employees in the IT department by 5000 rs.
    fix_salary="Salary"
    fix_department="Department"
    print("Updated Data Is:")
    print()
    for each in new:
        if each.get(fix_department)==" IT":
            sal=each.get(fix_salary)
            sal=sal+10000
            each.update({fix_salary:sal})
        for key,value in each.items():
            print(f"{key}:{value}")
        print()

# Identify and print employees with a salary above 70000.
    fix_salary="Salary"
    emp_name="Name"
    high_salary=[]
    print("Employees Names That Have More Salary Than 70000 :")
    print()
    for dic in new:
        if dic.get(fix_salary)>=70000:
            names=dic.get(emp_name)
            high_salary.append(names)
    for name in high_salary:
        print(name)
    print()



# Create a list of employees who work in the Marketing department.
    fix_depart="Department"
    fix_name="Name"
    print("Employees That Work In Marketing Department Is : ")
    market_list=[]
    for each in new:
        if each.get(fix_depart)==" Marketing":
            names=each.get(fix_name)
            market_list.append(names)
    for names in market_list:
        print(names)
    print()

# make a search option that user search data of employees based on their ages.
    fix="Age"
    try:                       #using try accept to avoid conflicts
      user_age_input=int(input("Enter Employee Age To Display His Details:"))
      for each in new:
          if each.get(fix)==user_age_input:
              for key,value in each.items():
                  print(f"{key}:{value}")
    except ValueError:
        print("You Entered Wrong age")
except FileNotFoundError:
    print("File Not Found")