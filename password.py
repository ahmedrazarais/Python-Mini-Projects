# printing Reqirements:
print("There are some requirements for setting a password.\n1. The pasword contains atleast 7 characters with one numeric digit and 1 special character is also acceptable..")
# taking input of password:
psd=(input("Enter Your Password:"))
# conditions:
if 7<len(psd)<15:
  if '0' or '1' or'2' in psd and '@' or '#' or '*' in psd:
    print("The Password you enter is valid!!") 
else:
    print("Invalid password")    