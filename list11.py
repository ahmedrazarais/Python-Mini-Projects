# Diagonal Sum:
# Calculate the sum of the main diagonal and the secondary diagonal of the matrix.
# initializing empty list first:
mat=[]
# applying loop for taking user input
for i in range(1,4):
    user=input(f"Enter Element of row {i} seperated by spaces:")
    user=user.split()
    user=[int(i)for i in user]
    mat.append(user)
print("You Enter Matrice:")
# printing matrice in standard form
print()
for i in mat:
    for x in i:
        print(x,end=" ")
    print()
print()    
print()    
# initializing empty diagnol matrice
diagnol=[]
# applying loop for taking diagnol elements from the users input matrice
for i in range(min(len(mat), len(mat[0]))):
# appending all diagnol elements in dignol list    
    diagnol.append(mat[i][i])
# calculating sum of diagnol matrice
total=sum(diagnol)
print("Diagnol elements are:")
print()
# printing diagnol elements
for i in diagnol:    
    print(i,end=" ")    
print()
# printing sum of diagnol elements
print(f"Sum Of Diagnol Elements is {total}")