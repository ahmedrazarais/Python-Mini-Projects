# Find the Maximum Element:
# Find the Minimum Element:
# Write a function to find the maximum value in the 2D list and print its position (row and column).

# usersinput
rows_no=int(input("Enter no of rows:"))
cols_no=int(input("Enter no of columns:"))
final=[]
for row in range(rows_no):
    sub=[]
    for column in range(cols_no):
        values=int(input(f"Enter Elements of row {row} and column {column}:"))
        sub.append(values)
    final.append(sub)
# printing in standrad form
for i in final:
    for j in i:
        print(j,end=" ")
    print()
# applying conditions for max and min
maximum=max(max(i)for i in final)
minimum=min(min(i)for i in final)
# applying conditions for checking conditions
position_max=[]
for i in range(len(final)):
    for j in range(len(final[i])):
        if final[i][j]==maximum:
          position_max.append((i,j))
position_min=[]
for i in range(len(final)):
    for j in range(len(final[i])):
        if final[i][j]==minimum:
            position_min.append((i,j))
print(f"MAXIMUM NO IS : {maximum} at position row and column {position_max}")
print(f"MAXIMUM NO IS : {minimum} at position row and column {position_min}")