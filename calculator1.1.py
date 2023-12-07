# MAKING AN EMPTY LIST FOR TAKING ALL INPUTS BY USER
values=[]  
num=int(input("Enter Number:"))
values.append(num)  
# APPLYING LOOP FOR TAKING SIGN AND NUMBER INPUT:
while True:
  sign=input("Enter Sign:")
#   APPLYING CONDITION IF SIGN=="=" SO LOOP WILL BREAK
  if sign=="=":
    break
  values.append(sign)
  num = int(input("Enter Number1: "))
  values.append(num)
# INITIALIZING ANSWER TO 0 INDEX OF LIST
answer = values[0]
# Using enumerate that it can iterate on both index and value of list
for i, value in enumerate(values):
    # checking that index of list is odd
    if i % 2 != 0:
        # Checking operators
        # using i+1 that after performing index will move to next index
        if value == "+":
            answer += values[i + 1]
        elif value == "-":
            answer -= values[i + 1]
        elif value == "*":
            answer *= values[i + 1]
        elif value == "/":
            answer /= values[i + 1]
# Printing Final answer            
print(f"Final Answer: {answer}")