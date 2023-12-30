# Task:

# Obtain a text file containing a list of integers, one per line.
# Read the file and create a list of integers from its contents.
# Identify and print the even numbers from the list.
# Calculate and print the sum of all odd numbers in the list.
# Create a dictionary that categorizes each number as "even" or "odd" and stores the count of each category.
# Write the categorized numbers and their counts to a new text file.


print("\tFILE MANIPULATION TASK")
#TAKING FILE NAME AS INPUT
file_name=input("Enter File Name To read Data From File:")
try:                         # USE TRY EXCEPT IF FILE NOT FOUND
   with open(file_name) as file:         #OPEN A FILE IN READ MODE
    contents=file.read().split()         # SPLITTING INTO LIST
    int_list=[]                          #MAKING AN INT_LIST EMPTY FOR APENDING DGITS

    for numbers in contents:    # APPLY LOOP TO COLLECT DIGITS  
        if numbers.isdigit():    # USING STRING MEHTOD
            int_list.append(numbers)    

    int_list=[int(i) for i in int_list]      # TYPE CATS INTO INTEGERS

    #MAKING EVEN AND ODD LIST USING LIST COMPREHENSION 
    even=[even for even in int_list if even %2==0]      
    odd=[odd for odd in int_list if odd %2 !=0]

    # CALCULATING SUM OF EVEN AND ODD
    total_odd=sum(odd)
    total_even=sum(even)

    #MAKING EMPTY DICTIONARIES FOR COLLECTING NUMBERS WITH THIER OCCURENCE
    dic_even={}
    
    #APPLY LOOP TO COUNT NUMBER WITH ITS OCCURENCE
    for i in even:
        occurence=even.count(i)
        number=i
        dic_even.update({number:occurence})      # UPDATE IN DICTIONARY
     
    #SAME WORK AS DO ABOVE
    dic_odd={}
    for i in odd:
        occurence=odd.count(i)
        number=i
        dic_odd.update({number:occurence})
    

# PRINTING ALL RESULT TO USER
    print(f"Even Numbers Occurence: {dic_even}")
    print(f"Odd Numbers Occurence: {dic_odd}")
    print(f"Total Numbers List Is :{int_list}")
    print(f"Even Numbers Are : {even}")
    print(f"Odd Numbers Are : {odd}")
    print(f"Sum Of ALL Odd Numbers Is : {total_odd}")
    print(f"Sum Of ALL Even Numbers Is : {total_even}")

except FileNotFoundError:
    print("File Not Found")

#TAKING NEW DESTINATION FILE INPUT
new_file=input("Enter File Name To Write Content In a file:")

#OPEN A FILE IN WRITE MODE
with open(new_file,"w+") as f:
    f.write("Even Numbers Along With Thier Occurences\n")
    for key,value in dic_even.items():
        f.write(f"{key}:{value}\n")

# WRITTING THE DATA OF BOTH EVEN AND ODD DICTIONARY
    f.write("\n")
    f.write("Odd Numbers Along With Thier Occurences:\n")
    for key,value in dic_odd.items():
        f.write(f"{key}:{value}\n")
    
