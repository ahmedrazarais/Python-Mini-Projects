# Make a program that a user is capable to enter email of employess and if he want to terminate he simply write quit
# make sure that email should not contain spaces dont write them in file if user write any
# duplicate email so send him a message that this is already added in lst and show him list


#printing users information
print("\t EMPLOYEES EMAIL ENTERIES")
print("Add email as much as you want simply write quit to terminate")
print("Dont Use Spaces Between EMail")


# Taking INput OF File By user
file=input("Enter File Name:")
with open(file,"a+") as f:                   # opening a file in a+ mode
    f.seek(0)                                # move cursor to start
    x=f.read().split()                       #split for making a list
    while True:                       # apply loop for taking input
        email=input("Enter Email OF Employee:")   
        if email=="quit" or email=="QUIT":        # apply condition for break
            break
        if email in x:                          # check if there is any duplicate enter
            print("It Is Already In A List")
            print()
            result=[i for i in x if i!=email]
            result.append(email)
            for each in result:
                print(f"Email :{each}")          # print the enitire list
        else:
          if " " not in email:            # apply condition that must not have space
           f.write(f"{email}\n")                # write in a file
           print(f"Email is added : {email}")            # print an email
          else:
             print("Email Should Not Contain Spaces")        # if it have space
        f.seek(0)                  # seek to move cursor start
        x=f.read().split()          # read a file and make a list
    for name in x:
        print(f"Email: {name}")               # printig final list