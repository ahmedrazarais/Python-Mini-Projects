# Task: Increment Numbers in a File
# # Create a text file named numbers.txt with a list of integers, each on a new line:
# Write a Python script that reads the numbers from the file, increments each number by a certain value (e.g., 3), and then writes the updated numbers back to the file.


print("\tNumber Increment Maker")
print("Enter Number as much as you want enter negative number to terminate then write the number for increment")

file_name=input("Enter File Name:")    # taking file name as input
with open(file_name,"w+") as file:          # opening a file in w+ mode
    while True:                    # applying loop for taking user input
        result=[]                # making an empty list for appending numbers in it
        try:                                    # using try except for value error
           number=int(input("Enter Numbers:"))       # taking input of numbers
           if number<0:       # breaking on certain condition
             break
           else:
             result.append(number)
             result=[str(i) for i in result]         # typecast in string to write in file
             for i in result:         
                 file.write(f"{i}\n")           # write in file
        except ValueError:
           print("Please Enter Numbers")
    file.seek(0)              # seek cursor to start
    x=file.read().split()       # splitt for making alist
    x=[int(i) for i in x ]            # typecast into integers
    try:                                                           
       inc_val=int(input("Enter The Number You Want To Do Increment of:"))       # asking number for increment
    except ValueError: 
       print("PLese Enter A digit")
    increment=[]             # qamking empty for appending increement values
    for i in x:
        z=i+inc_val
        increment.append(str(z))          # typecast to write in file
    file.seek(0)
    for i in increment:
     file.write(f"{i}\n")
    file.seek(0)                   # seek to move cursor to start
    print("Updated Numbers List are:")
    print(file.read())                   # printing aread file




