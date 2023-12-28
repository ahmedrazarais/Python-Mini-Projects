# make a program that read a content of a text file display total number of password along with passwords
# check password strngth along with conditions and chatgarezid them as weak strong and strongest
# check for common password
print("\t PASSWORD ANALYZER")

file_name=input("Enter File Name:")         # taking input of file name
try:
   with open(file_name) as file:           #opening a file 
    x=file.read()                               
    length=len(x.split())                    #checking length so we got total password
    print(f"There Are Total {length} Passwords and Ther are: \n{x}")
    print()
    file.seek(0)
    array=file.read().split()
    weak=[]
    strongest=[]
    strong=[]
    for check in array:                    # apply conditions for passwords and appending them on their respective list
        if len(check)<8:
            weak.append(check)
          
            
        elif len(check)>8 and any(char.isdigit() for char in check) and any (not (char.isalnum()) for char in check):
            strongest.append(check)
          
        elif len(check)>=8 and any(char.isdigit() for char in check):
            strong.append(check)
    
    if weak:
        print("Weak Password are:")
        for i in weak:
            print(i) 
        print()
            
    if strongest:
          print("Strongest Password are:")
          for i in strongest:
            print(i) 
          print()
    if strong:
          print("Strong Password are:")
          for i in strong:
            print(i)
          print() 
  
    double=[i for i in array if array.count(i)>1]          #using list comprehension for checking common passwords
    print("Common Passwords are:")
    for check in double:
        print(check)
except FileNotFoundError:
    print("This File Is Not Found")
                      

        