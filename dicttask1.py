# Accessing Values:
# Access a value in the dictionary using its key.
# Try to access a key that does not exist and handle the KeyError.
# printing information to user about how to complete thier dictionary
print("Enter Your Favourite Programming Language and thier synatx when you want to quit press q or Q ")
# initializing empty dictionary
dic={}
# applying loop for taking user_input
while True:
    lang_name=input("Enter Your programming Name:")
    if lang_name=="Q" or lang_name=="q":
        break
    else:
        syntax_name=input("Enter favourite syntax Name:")
        # taking all values in form of keyvalue pair in dictionary
        dic.update({lang_name:syntax_name})
# printing user_dictionary        
print(f"YOUR DICTIONARY IS: {dic}")
# asking user which item he wants to acess
ask=input("Which Item You Want To acess:")
# applying condition to checking key is in dictionary or not
if ask in dic:
    y=dic.get(ask)
    print(y)
else:
    print("There Is no Item Of that Key")