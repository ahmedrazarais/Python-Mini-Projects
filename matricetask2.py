# Write code to print a matrix in matrix form (except the square brackets) on the screen

# asking user fr no of rows and columns
row_no=int(input("Enter No of rows:"))
col_no=int(input("Enter No of columns:"))
# APLLYING LLOP FR TAKING INPUT:
Mat=[]
for row in range(row_no):
    sub=[]
    for col in range(col_no):
        values=int(input(f"Enter Element of row {row} and column {col}:"))
        sub.append(values)
    Mat.append(sub) 
print()     
# NOW PRINTING MATRICE IN STANDARD FORM:
print("MATRICE:") 
for row in  Mat:
    for col in row:
        print(col,end=" ")
    print()           
