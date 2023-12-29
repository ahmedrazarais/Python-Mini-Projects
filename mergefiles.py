# Certainly! Here's another task for you:

# Task: Merge Files using Functions

# Create a function called merge_files that takes two file names as input. The function should read the content of both files and write the combined content into a new file.

# In the main part of your program, prompt the user to enter the names of two text files. Ensure that these files exist, and if not, create them and ask the user to input some text for each file.

# Call the merge_files function with the names of the two files.

# After merging, create another function called read_merged_file that takes the name of the merged file as input and prints its content.

# Call the read_merged_file function with the name of the merged file to verify the content.

# This task will help you practice reading from files, creating functions, and combining their functionality. Feel free to ask for clarification or assistance if needed!


print("\tMeege Files Using Functions")
# TAKING EMPTY LIST
user=[]
file1=input("Enter  first File Name :")            #TAKING INPUTS OF FILENAMES
file2=input("Enter second File Name:")
new_file=input("Enter Destination file:")
def merge_files(file1,file2,new_file,user):         # DEFINE FUNCTIONS FOR FILE1 FILE2 NEW FILE 
    with open(file1,"r+") as f1:                    # OPEN IN R+MODE
        contents1=f1.read().strip()
        if contents1:                    #IF ALREADY HAVE CONTENTS
            print(contents1)
        else:
            user_write=input("Write contents for file1:")     #give prompt to write in file
            f1.write(user_write)
            user.append(user_write)
    with open (file2,"r+") as f2:             #SAME WITH SECOND FILE
        contents2=f2.read().strip()
        if contents2:
            print(contents2)
        else:
            user_input=input("Write contents for file2:")
            f2.write(user_input) 
            user.append(user_input)
    with open(new_file,"w+") as f3:     # OPEN A FILE FOR MERGING CONTENTS
        for i in user:
         f3.write(f"{i}\n")                #WRITE MEGERLY
         print(f"Merged Contents written in a {new_file}")
merge_files(file1,file2,new_file,user)          # CALLING A FUNCTION


def read_merged_file(new_file):             #ANOTHER FUNCTION FOR READNG MERGED CONTENTS
    with open(new_file) as file:
        contents=file.read()
    print(f"contents of merge file is {contents}")        #PRINTING CONTENTS OF MERGED FILE
read_merged_file(new_file)           # CALLING A FUNCTION