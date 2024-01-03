# Create a text file named "input.txt" and write a list of numbers (one number per line).
# Write a Python program to read the "input.txt" file, calculate the sum of the numbers, and then write the result to a new file named "output.txt".
# Execute your Python program and verify that "output.txt" contains the correct sum of the numbers from "input.txt".

file_name=input("Enter Source FIle Name:")      # TAKING FILE NAME INPUT
num_list=[]        #MAKING A LIST TO APPEND ALL VALUES IN LIST
print("Enter Numbers Enter 0 To Terminate")
#APPLYING LOOP TO TAKE INPUT INFINITE TIMES
while True:
    num=input("Enter Numbers:")
    #APPLY CONDITION ON THAT SHOULD BE DIGIT
    if num.isdigit():
     if num=="0":
        break     # BREAK ON CONDITION
     else:
        num_list.append(num)             # APPENDING IN LIST
    else:
       print("Please Enter Numbers")
print("Numbers Entered Are:")     
for i in num_list:            # PRINTING NUMBERS
    print(i,end=" ")
print()

with open(file_name,"w+") as file:       # OPEN FILE TO WRITE NUMBERS LINE BY LINE
    for i in num_list:
        file.write(f"{i}\n")
    file.seek(0)
    sum_list=[]        # MAKING LIST SO GET ALL NUMBERS IN LIST FOR CALCULATING SUM
    for line in file:
        sum_list.append(line)
    sum_list=[int(i) for i in sum_list]       # TYPECAST INTO INTEGER
    total=sum(sum_list)
    print(f"Sum Of Numbers is :{total}")
new_file=input("Enter Destination File to write Sum In File:")


# OPEN DESTINATION FILE AND WRITE IT SUM INTO IT 
with open(new_file,"w") as new:
    new.write(f"sum Of Numbers Are {total}")


    