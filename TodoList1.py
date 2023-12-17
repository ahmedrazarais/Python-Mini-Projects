# MAKE A TODOLIST THAT CONTAIN FOLLOWING 3 FUNCTIONS FOR USERS
# ADD,UPDATE,DELETE,END
print("Here Is a short  online saver for you where you can add update or delete your tasks")

dic={}                 # initializing empty dictionary      
while True:          # Applying loop for asking users choice
    while True:          # applying another loop for looking user enter correct word or not
      ask=input("Enter What you want to do [add/update/delete/end]:")
      ask=ask.lower()      #   converting in lower
      if ask=="add" or ask=="update" or ask=="delete" or ask=="end":
        break
      else:
        print("You Entered Wrong Keyword")
        print("Write [add,update,delete,end] ") 
        print()    
    # checking conditions now    
    if ask=="add":
      task=input("Enter Your Task :")
      dic.update({len(dic)+1:task})
      print(f"your list is {dic}") 
    elif ask=="update":   
     dic
     print(f"Your list is : {dic}")
     key=int(input("Write key whose value you want to change: "))   #Ask user which key
     task=input("Write what you want to update in replacement:")    #ask userenter value
     for check in dic:    #applying loop to checking keys
         if key==check:    #Checking if key ==check
            dic.update({key:task})
            print(f"Your Modified List is {dic}")
     if key not in dic:
       print("You Entered Wrong Key")  
       print(f"Your list is {dic} kindly look properly on keys")  
       found=False
    elif ask == "delete":
     print(f"Your list is : {dic}")
     key = int(input("Which task do you want to delete:"))
     found = False  # initializing found to false
     if key in dic.keys():
        for i in dic.copy().keys():      # Create a copy of the dictionary keys to iterate over
            if i == key:          #checking if user enter value is in key
                del dic[i]        # Deleting an order pair
                found = True      # initializing found to True
        if found:
            print(f"Your modified List is : {dic}")
     else:
        print("You Entered Wrong Key")
        print(f"Your list is : {dic} kindly look properly on keys")      
    elif ask=="end":
      dic
      print("Program is finished")
      print("Your Entire Response is",dic)
      break
     #To come out of program loop
    
      




      
