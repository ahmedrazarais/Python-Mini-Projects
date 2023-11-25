# MAKING APROGRAM THAT TELL USER WHAT ARE VOWELS AND HOW MANY VOWELS IN THAT LINE AND THE PRINT ITS TABLE:
# MAKING EMPTY LIST:
vowels=[]    
# INITIALIZIG COUNT==0:
count=0
word=input("Enter The line:")
# APPLYING LOOP FOR CHECKING VOWELS
for ch in word:
    if ch in "aeiouAEIOU":
        count=count+1
        vowels.append(ch.lower())
    elif ch not in "aeiouAEIOU":
        count==0
# Printing Result of number of vowels and vowels        
print(f"TOTAL VOWELS ARE :{count}")        
print(f"The Vowels Are {vowels}")
# printing table of total counts:
for i in range(1,11):
    print(count,"*",i,"=",count*i)