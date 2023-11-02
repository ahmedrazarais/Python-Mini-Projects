# Telling conditions for output:
print("if score >30 output is kamran akmal")
print("if 20<score<30 output is shoaib akhtar")
print("if 10<score<20 output is shahid afridi")
# taking input:
score=int(input("Enter Your Score:"))
# Apply conditions:
if score>30:
    print("Kamran Akmal")
elif 20<score<30:
    print("Shoaib Akhtar")    
elif 10<score<20:
    print("Shahid afridi") 
else:
    print()          
