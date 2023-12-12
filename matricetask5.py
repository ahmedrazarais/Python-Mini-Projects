# 15. Write code to add two matrices of similar dimensions, storing the result in a new matrix
# Input dimensions of both matrices
rows_1 = int(input("Enter the number of rows for matrice 1: "))
columns_1 = int(input("Enter the number of columns for matrice 1: "))
rows_2 = int(input("Enter the number of rows for matrice 2: "))
columns_2 = int(input("Enter the number of columns for matrice 2: "))

# Check if dimensions are equal before proceeding
if rows_1 != rows_2 or columns_1 != columns_2:
    print("Dimension of matrices should be equal for addition")
else:
    # Create empty matrices
    matrice_1 = []
    matrice_2 = []

    # Input elements for matrice 1
    for i in range(rows_1):
        sub = []
        for j in range(columns_1):
            values = int(input(f"Enter element of row {i} and column {j} of matrice 1: "))
            sub.append(values)
        matrice_1.append(sub)

    # Input elements for matrice 2
    for i in range(rows_2):
        sub = []
        for j in range(columns_2):
            values = int(input(f"Enter element of row {i} and column {j} of matrice 2: "))
            sub.append(values)
        matrice_2.append(sub)

    # Calculate and print the sum matrix
    sum_mat = []
    for i in range(rows_1):
        mini = []
        for j in range(columns_1):
            val = matrice_1[i][j] + matrice_2[i][j]
            mini.append(val)
        sum_mat.append(mini)

    print("Sum of matrices:")
    for row in sum_mat:
        for col in row:
            print(col, end=" ")
        print()

              
 