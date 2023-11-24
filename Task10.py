# # MAKE A PRGRAM THAT TAKE INPUT BY USER OF THIER FULL NAME THEN PRINT THE TABLE OF TOTAL LETTERS IN THIER NAME(SPACES DONT COUNT)
# # DONT USE LENGTH FUNCTION:

# # TAKING INPUT OF USER_NAME:
full_name=input("Enter Your Full Name:")
# # INITIALIZIG COUNT TO ZERO:
count=0
# # APPLYING LOOP TO COUNT LETTERS IN NAME:
for ch in full_name:
    if ch!=" ":
        count+=1       
    else:
        # USE CONTINUE TO AVOID SPACES
         continue        
# # ASSIGNINGING VARIABLE TO TEN TO PRINT TABLE TO 10:         
x=10    
# APPLYING LOOP TO PRINT TABLE:
for num in range(1,x+1):
    print(count,"*",num,"=", count*num)