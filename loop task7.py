# FINDING COMMON AND UNCOMMON ELEMENTS IN BOTH STRINGS
# TAKING INPUT BY USER:
string1=input("Enter The String:")
string2=input("Enter The String:")
# MAKING EMPTY LIST:
common_elements=[]
uncommon_elements=[]
# APY CONDITIONS FOR COMMON ELEMENTS:
for ch in string1:
    if ch in string2:
       common_elements.append(ch)
# APPLYING CNDITIONS for UNCOMMON ELEMENTS:       
for ch in string1:
    if ch not in string2:
            uncommon_elements.append(ch)
for ch in string2:
     if ch not in string1:
          uncommon_elements.append(ch)
# PRINTING BOTH COMMON AND UNCOMMON ELEMENTS                                
print(f"COMMON ELEMENTS: {common_elements}")        
print(f"UNCOMMON ELEMENTS : {uncommon_elements}")        





    