# 8. Write code to add up and print all the positive values in a list of integers. For example, a list containing the elements
# [3,-3,5,2,-1,2] would evaluate to 12, since 3+5+2+2 = 12. The code prints zero if the list is empty.




# TAKING USERINPUT:
user_input=input("Enter List seperated by spaces:")
# SPLITING INTO CHUNKS 
user_input=user_input.split()
# TYPEECASTING THE LIST ELEMNTS STRING INTO INTEGERS
int_list=[int(i)for i in user_input]
# MAKING AN EMPTY LIST FOR TAKING POSITIVE VALUE
positive=[]
# APPLYING LOOP FOR CALCULATING SUM
for i in int_list:
    if i>0:
        # APPLY CONDITION THAT IF i >0 SO APPEND IN NEW LIST
        positive.append(i)
        # CALCULATING TOTAL
        total=sum(positive)
# APPLY CONDITION FOR CHECKING IF LIST IS EMPTY        
if len(int_list)==0:
     print("Zero")
# PRINTIG SUM ELSE     
else:
    print(f"SUM : {total}")