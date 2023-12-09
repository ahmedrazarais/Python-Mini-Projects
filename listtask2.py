# 9. Write code that counts and prints the even numbers in a list of integers. For example, a list containing the elements
# 3;5;4;-1; and 0, would evaluate to 2, since there are only two even numbers: 4 and 0. The code prints zero if the list is
# empty. 



user_input=input("Enter List of number:")
user_input=user_input.split()
int_list=[int(i) for i in user_input ]
even=[]
odd=[]
# applying loop for checking even numbers
for i in int_list:
    if i%2==0:
        even.append(i)  
# applying conditions for odd        
for i in int_list:
    if i % 2 !=0:
        odd.append(i)

if len(int_list)==0:
    print("Zero")
else:
    # calculating how many even numbers are there
    z=len(even)
    x=len(odd)
    print(f"There are total {z} even numbers in list and they are {even}")
    print(f"There are total {x} odd numbers in list and they are {odd}")