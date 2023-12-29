# Create a function called write_to_file that takes a file name and a list of strings as input. The function should write each string to the file on a new line.
# Create another function called read_from_file that takes a file name as input and reads the content of the file. The function should print each line of the file.
# In the main part of your program, prompt the user to enter multiple strings until they enter an empty string. Store these strings in a list.
# Call the write_to_file function with the user-entered strings and a file name of your choice.
# Call the read_from_file function with the same file name to print the content of the file
# This task will allow you to practice writing and reading from files using functions in Python. Feel free to ask for clarification or assistance if needed!





user=[]      # making an empty list
file=input("Enter File Name:")    # taking input of file name

# define function write to file
def write_to_file(file,user): 
#open a file in write mode
    with open (file,"w") as f:
        while True:        # take input by user
            strings=input("Enter The Lines:")
            if len(strings)==0:    # break on certain condition
                break
            else:
                user.append(strings)       # appending all in a list
        for i in user:
                f.write(f"{i}\n")          # write to file the values in list
write_to_file(file,user)                  # call a function

def read_from_file(file):             # another define function read from file
    with open (file) as f:
        contents=f.read()         # reading the contents
        print(contents)           # printing the contents
read_from_file(file)              # call the frunction