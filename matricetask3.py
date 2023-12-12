# 13. Write code to increment a matrix, storing the result in a new matrice
matrice=[]
rows=int(input("Enter No of rows:"))
columns=int(input("Enter No of columns:"))
for i in range(rows):
    sub=[]
    for j in range(columns):
        values=int(input(f"Enter Elements of row {i} and column {j}:"))
        sub.append(values)
    matrice.append(sub)
print("YOUR MATRICE:")
for row in matrice:
    for col in row:
        print(col,end=" ")
    print()
# initializing empty list for sum
result=[]
# INCREMENT IN MATRICE:
for i in range(len(matrice)):
    sub=[]
    for j in range(len(matrice[0])):
       val=matrice[i][j]+1
       sub.append(val)
    result.append(sub)      
# now showing resultant matrice in standard form
print("RESULTANT MATRICE:")
for x in result:
    for y in x:
        print(y,end=" ")
    print()                       