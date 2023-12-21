# 5. Write Python program to read the file created after calculating average and print average of the numbers. by user input
final=[]        # making an empty list
print("Enter The values write quit to terminate")
while True:
    values=input("Enter The integers :").lower()   # atking input as str as user write quit to exit
    if values=="quit":
       break
    else:
         final.append(int(values))     # appending values in list with typecasting

#opening a file
avg_file=open("C:/Users/ideal pc/Desktop/ComuterProgramming/ComputerProgramming/average.txt","w+")

average=sum(final)/len(final)         # calculating average
avg_file.write(str(average))       # typecast in string as write accept only string
avg_file.seek(0)              # seek to read from start
print(f"Average of Numbers are : {avg_file.read()}")      # read a file
avg_file.close()             # close the file
