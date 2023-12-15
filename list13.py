# Check for Symmetry:
# Write a function to check if the matrix is symmetric.

# Taking user input
matrice=[]
row_no=int(input("Enter No of Rows:"))
col_no=int(input("Enter No of Columns:"))
for i in range(row_no):
    sub=[]
    for j in range(col_no):
        values=int(input(f"Enter Elements of row {i} and column {j}:"))
        sub.append(values)
    matrice.append(sub)
# printing matrice in standard form
print("Matrice:")
print()    
for i in matrice:
    for j in i:
        print(j,end=" ")
    print()
print()
# taking transpose of matrice
transpose=[]
for i in range(col_no):
    sub=[]
    for j in range(row_no):
        result=matrice[j][i]
        sub.append(result)
    transpose.append(sub)
# printing transpose in standard form    
print("Transpose of matrice:")
print()
for i in transpose:
    for j in i:
        print(j,end=" ")
    print()
# Applying conditions for checking symmetrical:
print()
if matrice==transpose:
    print(" The Given Matrice is Symmetrical")
else:
    print(" The Given Matrice is Not Symmetrical")            