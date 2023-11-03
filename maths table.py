# Taking input by user of number:
number=int(input("Enter Your Number:"))
# Applying loop:
print(f"The Multiplication table of {number}:")
for i in range(1, 11):
    table=number*i
    # print final result:
    print(f"{number}*{i}={table}")
