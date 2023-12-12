# 11. Write code to take integer inputs from user to form a 3x3 matrix.

# MAKIG EMPTY LIST:
Matrice=[]
#  APPLY LOOP FOR TAKING INPPUT BY USER OF 3X3 MATRICE
for i in range(3):
    # ASKING USER T ENTER VALUES
    values=input("Enter Elements row wise seperated by spaces:")
    values=values.split()
    # TYPEASTING INTO INTEGER
    values=[int(i) for i in values]
    Matrice.append(values)
# NOW DISPLAYING Matrice INTO STANDARD FORM:
for row in Matrice:
    for col in row:
        print(col,end=" ")
    print()    
