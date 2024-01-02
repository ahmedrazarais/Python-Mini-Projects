# Write a Python program that does the following:
file_name=input("Enter SOurce FIle Name To Acees Data:")
try:
   with open(file_name) as file:
    final=[]
    for line in file:
        data=line.split()
        user_dic={"NAME":data[0]+data[1],"AGE":int(data[2])}
        final.append(user_dic)
    for dic in final:
       for key,value in dic.items():
          print(f"{key}:{value}")
       print()

# b. Calculates and prints the average age of the users
    user_Age=[]
    fix="AGE"
    for dic in final:
      age=dic.get(fix)
      user_Age.append(age)
    avg_age_users=sum(user_Age)/len(user_Age)
    print(f"Average Age Of All Users Is : {avg_age_users}")

# c. Asks the user to enter a name. If the name is in the dictionary, print the age of that user. If not, inform the user that the name is not found.
    fix_name="NAME"
    fix_age="AGE"
    user_name_input=input("Enter The Name Of User To Get Age Of User:").lower()
    found=False
    for dic in final:
           if dic.get(fix_name).lower()==user_name_input:
             found=True
             print(f"Age Of {user_name_input} Is {dic.get(fix_age)}")
    if not found:
       print("No Record Found OF That Name")

# d. Prints the names and ages of users who are older than 25.
    fix_name="NAME"
    fix_age="AGE"
    names=[]
    for dic in final:
        if dic.get(fix_age)>25:
            name=dic.get(fix_name)
            names.append(name)
    print("Users Older Than  Age 25 :")
    for every in names:
       print(every)
    print()
            
         
# e. Writes a new text file named user_info_updated.txt with the same information as the original file, but each age increased by 1.     
    new_file=input("Enter Destination File Name With Extension To Write Updated Data:")
    with open(new_file,"w") as upd_file:
     fix_age="AGE"
     for dic in final:
       new_age=dic.get(fix_age)
       new_age+=1
       dic.update({fix_age:new_age})
       for key,value in dic.items():
          upd_file.write(f"{key}:{value}\n")
except FileNotFoundError:
   print("File Not Found Try Again!")          
       
       

    
     
     

 