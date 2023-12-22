# 3. Write a function fcopy that takes as input two file names (as strings) and copies the content of the first file into the
# second line by line.

def fcopy():      #defining function
    file_1=input("Enter file 1:")      #taking input
    file_2=input("Enter file 2:")      # taking input

    new=open(file_1)       #opening a file
    new.read()              #reading afile
    old=open(file_2,"w+")           
    new.seek(0)         # move cursor to start
    for line in new.readlines():       #iterating for reading lines
        old.write(line)              # write content in second file

    old.flush()                       
    old.seek(0)
    print(old.read())                    #printing file contents
    
    new.close()                 # closing file
    old.close()                  # closing file


fcopy()               # calling the function
