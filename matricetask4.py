# 14. Write code to increment a matrix, storing the result in the same matrix
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
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        matrice[i][j]=matrice[i][j]+1
print("RESULTANT MATRICE:")
for rows in matrice:      
    for col in rows:
        print(col,end=" ")
    print()    
