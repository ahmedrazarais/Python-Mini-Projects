# FINDING LARGEST INTEGER THAT INPUT BY USER
# making empty list:
values=[]
# TAKIG INPUT  BY USER OF INTEGERS:
integer=int(input("Enter list:"))
# TYPECAST INTEGER INTO STRING BECAUSE INT IS NOT ITERABLE:
integer_str=str(integer)
# APPLYING LOOP FOR ITERATON
for i in integer_str:
    # CONVERTING ALL VALUES INTO LIST:
    values.append(i) 
# PRINTING LIST TO SHOW THE LIST    
print(values)   
# FNDING MAX NUMBER IN LIST
max_value=max(values)
# PRINTING RESULT OF LARGEST INTEGER
print(f"LARGEST INTEGER: {max_value}")



