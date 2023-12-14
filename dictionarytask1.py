# QUESTION:
# MAKE A PROGRAM THAT ALLOWS USER TO ENTER ROLL NO AND STUDENTS NAME S MANY TIME
# AS HE WANTS BUT WHEN HE ENTER Q OR q IT WILL TERMINATE THEN ASK USER DID YOU WANT
# TO SEE DATA IF HE SAY YES SHOW HIM IN STANDARD FORM IF NO DONT SHOW DATA IN BOTH CASES 
# YES OR NO YU ASK AGAIN USER THAT IF H WANT TO ADD MORE DATA OR NOT MEANS USER HAVE A
# CHANCE TO ENTER 2 TIMES DATA AFTER THAT PROGRAM SHOULD ENDED IF HE SAY NO SECOND TIME
 
print("You have 2 chances to enter your data in this program")
print("Enter Your students data and write q or Q to complete execution")
print()
# initializing empty list
l=[]
# initializing empty dictionary
dic={}
# appling loop for taking user_input as he able to input his desired ones 
while True:
      roll_no=input("Enter roll no of student:")
      if roll_no=="q" or roll_no=="Q":
         break
      else:
         name=input("Enter Student name:")
         dic.update({roll_no:name})
# AGAIN APPLYING LOOP FOR ASKING IF HE WANTS TO SEE DATA OR NOT         
while True:
             ask=input("Did You see the data?:[Yes/No]:")
             ask=ask.upper()
             if ask=="YES" or ask=="NO":
                 break
             else:
                 print("Please Enter Correct word")
# APPYING CONDITIONS FOR CHECKING USER WANTS TO SEE DATA OR NOT                 
if ask=="YES":
  l=[]
  for i in dic.items():
    l.append(i)
  print("You Entered This data:")
  print()  
  for i in l:
    for j in i:
        print(j,end=" ")
    print()                    
elif ask=="NO":
    print("ALRIGHT")
# applying loop for asking if he wants to add more data    
while True:
    more_add=input("Did You Want to add more data?[YES/NO]:")
    more_add=more_add.upper()
    if more_add=="YES" or more_add=="NO":
        break
    else:
        print("Plese Enter correct word")
# conditios if he want to see data or not        
if more_add=="YES":
    print("Enter Your students data and write q or Q to complete execution")
    dic_2={}
    while True:
      roll_no=input("Enter roll no of student:")
      if roll_no=="q" or roll_no=="Q":
         break
      else:
         name=input("Enter Student name:")
         dic_2.update({roll_no:name})
      final=[]        
    #   combining both dictionaries
      dic.update(dic_2)
    #   applying loop to append dictionary values in list
    for i in dic.items():
     final.append(i)
    #  applying loop to print list value in standard form
    print("Your Complete data is:")
    print()
    for i in final:
     for j in i:
        print(j,end=" ")
     print()  
elif  more_add=="NO":
    print("PROGRAM has Finished!")  