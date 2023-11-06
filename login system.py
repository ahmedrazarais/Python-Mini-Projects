# Making a login system:
# giving information to user:
print("Gmail id must contains atleast 7 characters\nAND 2,3 digits and atleast one special character ")
print("The Length of Password must be greater than 5 and make your pasword stronger")
gmail=(input("Enter your Gmail ID:"))
psd=(input("Enter your Password:"))
# conditions for gmail:
if len(gmail)>7:
    if "0123456789" or "!@#$%^&*" or "." in gmail:
        print(f"Your Gmail ID is:{gmail}")
# conditions for password:
if len(psd)>5:
        if "0123456789" or "!@#$%^&*"  in psd:
               print(f'you got strong password:{psd}' )      
else:
    print("Invalid 'you might not fulfill all conditions'")               




    
          
         
      
    
