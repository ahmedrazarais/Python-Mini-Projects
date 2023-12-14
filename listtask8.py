# PRACTICING 2D LIST
print("Here is a short game that if any pattern of your input is same you win either lose")
t=[]
for i in range(3):      
    user_input=input("Enter Element row wise ['x' or 'o']:")     
    user_input=user_input.split()
    t.append(user_input)
for i in t:
    if  t[0][0]==t[0][1] and t[0][1]==t[0][2] and t[0][0]==t[0][2]:
      print(f"'{t[0][0]}'")
      break
    elif  t[1][0]==t[1][1]  and t[1][1]==t[1][2] and t[1][0]==t[1][2]:
        print(f"'{t[1][0]}'")
        break
    elif  t[2][0]==t[2][1] and t[2][1]==t[2][2] and t[2][0]==t[2][2]: 
        print(f"'{t[2][0]}'")
        break   
    elif t[0][0]==t[1][0] and t[0][0]==t[2][0] and t[1][0]==t[2][0]:
        print(f"'{t[0][0]}'")
        break
    elif t[0][1]==t[1][1] and t[0][1]==t[2][1] and t[1][1]==t[2][1]:
        print(f"'{t[0][1]}'")
        break
    elif t[0][2]==t[1][2] and t[0][2]==t[2][2] and t[1][2]==t[2][2]:
       print(f"'{t[0][2]}'") 
       break
    elif t[0][0]==t[1][1] and t[0][0]==t[2][2] and t[1][1]==t[2][2]:
      print(f"'{t[0][0]}'")
      break
    elif t[0][2]==t[1][1] and t[0][2]==t[2][0] and t[1][1]==t[2][0]:
      print(f"'{t[0][2]}'")
      break
    else:
       print('"No Pattern Match"')
       break