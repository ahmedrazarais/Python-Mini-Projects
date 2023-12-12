# 17. Write code to transpose a matrix, storing the results in a new matric.

# taking input by user of matrice of rows and columns
row_no=int(input("Enter No of Rows:"))
col_no=int(input("Enter No of columns:"))
# initializing empty matrice
matrice=[]
for row in range(row_no):
    sub=[]
    for j in range(col_no):
        values=int(input(f"Enter elements for row {row} and column {j}:"))
        sub.append(values)
    matrice.append(sub)
print("YOUR MATRICE:")
# printing matrice in standard form
for i in matrice:
    for j in i:
        print(j,end=" ")
    print()


# NOW TAKING TRANSPOSE
transpose=[]
for i in range(col_no):
    sub=[]
    for j in range(row_no):
        trans=matrice[j][i]
        sub.append(trans)
    transpose.append(sub)
print("TRANSPOSE OF MATRICE:")
# printing transpose in standard form:
for x in transpose:
    for y in x:
        print(y,end=" ")
    print()            