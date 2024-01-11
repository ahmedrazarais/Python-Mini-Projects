#MAKE A SMALL VALIDATION FOR GMAIL AND PASSWORD FOR USER


print("Here Is A Program But You Have To Enter Your Gmail And Password First")
while True:
                gmail_=input('Enter your gmail:')
                s='!#$%^&*()_+|}{":<?/,\';\\][=-]}'
                if gmail_=='':
                    print('Required field cannot be left blank')
                elif gmail_.startswith(' '):
                    print('The entered gmail is not valid')
                elif not(6<len(gmail_)<30):
                    print('Length must be between 6 and 30 characters long')
                elif not(gmail_.endswith('@gmail.com')):
                    print('Make sure @gmail.com must be at last')    
                elif (gmail_.startswith('@gmail.com')):
                    print('Enter valid Gmail')
                elif (gmail_.endswith('.@gmail.com')):
                    print('Sorry the last character before @gmail.com must be a letter or number')
                elif any(char in s for char in gmail_):
                        print('Only letters and numbers are allowed')
                else:
                    break
while True:
                    password = input("Enter Your Password: ")
                    
                    if any(char.isdigit() for char in password) and any(not (char.isalnum()) for char in password) and len(password) >= 8:
                          break
                    else:
                          print("Password Must Be Strong With Atleast 1 2 Digits And A special character")
