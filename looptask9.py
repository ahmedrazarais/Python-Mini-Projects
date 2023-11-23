# PRINTING SPIRAL PATTERN
n=int(input("Enter Number Of Lines:"))
for i in range(1,n+1):
    print(i*'*')
for j in range(n+1,0,-1):
    print(j*'*')   








x=int(input("Enter the number:"))
for i in range(1,x+1):
    for j in range(x+1,i,-1):
        print("*",end="")
    print()        




z=int(input("Enter Line:"))
for rows in range(1,z+1):
    for columns in range(1*z):
        print('*',end="")
    print()        