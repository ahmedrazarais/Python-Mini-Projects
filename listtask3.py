# checking that user enter list is in ascending order or not

# Taking user iput    
user_input=input("Enter List of number:")
user_input=user_input.split()
# typecasting into integer
int_list=[int(i) for i in user_input ]
# making a copy of list
x=int_list[:]
y=int_list[:]
# sort in decending order
y.sort(reverse=True)
# sort in ascending order
x.sort()
# checking condition if list in ascending order
if int_list==x:
    print("List in ascending order")
# checking condition if list in descending order    
elif int_list==y:
    print("List In Descending order")   
# checking condition if list not in ascending or descending order     
else:
    print("List is not in either ascending or descending order")   