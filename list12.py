# Count Occurrences:
# Write a function to count the occurrences of a specific element in the 2D list.
# using split mehtod necessary
# give user range of 3



# initialzing empty list
mat=[]
# applying loop for taking users data
for i in range(3):
    user=input("Enter elements row wise seperated by spaces:")
    user=user.split()
    user=[int(i)for i in user]
    mat.append(user)
print("Entered Elements are:")
# printing list in standard form
print()    
for i in mat:
    for j in i:
        print(j,end=" ")
    print()
# asking user which element occurence he want to chcek    
ask=int(input("Which element's occurence did you want to check?:"))
print()
# initializing count==0
count=0
# applying loop for checking conditions
for i in mat:
    for j in i:
      if ask == j:
        count+=1
# printing count if it is greater than zero        
if count>0:
    print(f"{ask} exist in your data ant the total count is {count}")
else:
    print("Number Not exist in data") 