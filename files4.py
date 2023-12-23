# # 4. Implement function distribution that takes as input the name of a file (as a string). This one-line file will contain
# # letter grades separated by blanks. Your function should print the distribution of grades.
# # Test Data:
# # >> distribution('grades.txt')
# # 6 students got A
# # 2 students got A3 students got B+
# # 2 students got B
# # 2 students got B4 students got =0


file=("C:/Users/ideal pc/Desktop/ComuterProgramming/ComputerProgramming/grades.txt")
def distribution(file):     #defining a function           
    file=open(file)                            # opening file
    x=file.read()       #read a file
    x=x.split()         # splitting to make a list
    dic={}           #making empty dictionary
    for grade in x:     #loop for checking grades and occurence
        grades=grade
        occurence=x.count(grades)
        dic.update({grades:occurence})          # updating values in dictionary
    for i in dic.keys():           # loop on dic keys
        print(f"{dic.get(i)} students got {i}")          # printing details

    file.close()                   # closing a file

distribution(file)               # call a function





























# 1 student got C2 students got F
