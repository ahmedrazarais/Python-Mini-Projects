# MAKING A USER'S'FRIENDLY PROGRAM THAT HE IS CAPABLE OF BOOKING FARMHOUSE OR CRUISE 
# AND SELECT MORE CHOICES FOR ENTERTAINMENT 
# WE GIVE SEVERAL INFORMATION TO HIM THAT HE CAN CHOICE WHAT HE WANT
# INITIALIZING ALL VARIABLES FOR CALCULATIOnS
total = 2500
qawwali=1000
cricket=2000
bbq=500
cruise=5000    
candlelight=2000
concert=1500
# Making an empty list for calculatin sum
expense=[]
# printig information
print("HEY THERE IS RABA @ CO EVENT MANAGEMENT TEAM\t\t\t\t")
print("WE PROVIDE YOU 2 CHOICES THAT WILL SURELY ENTERTAIN YOU")
print("1.BOOK YOUR OWN FARMHOUSE")
print("2.ENJOY CRUISE DINNER")
print("3.To Exit The Program")
print()
name=input("Enter Your Full Name:")
# applying loop for takig user choice of booking farm or cruise
while True:
    choice=int(input("Enter Your Choice from [1.(Book Farmhouse) 2.(Book cruise) 3. (Exit The Program)]:"))
    if choice==1 or choice==2:
        break
    # aplly if user direct enter 3 to exit program
    elif choice==3:
        print("Program is Finished!")
        break
    else:
        print("please Enter Correct choice") 
# apllying conditions for booking farmhouse        
if choice == 1:
    print(f"{name}, There is Raba Farmhouse In the town")
    print("Here are Few Details For you:")
    print("Per Day charges for farmhouse==2500")
    print("Extra expenses are based on your choices")
    print(f"{name} We are glad to serve you! Let us know Your Requirements")
    print()
    # calculating rent of farm
    time = int(input("Enter For How many days you want to book?:"))
    rent = total * time
    # append all values to empty list
    expense.append(rent)
    print(f"Total rent for your {time} Days is ['{rent}'] Pkr")
    print()
# printing extra infrmation for entertainment
    print('''Here are more options that can entertain you!
        1. Qawwali night(charges==1000)
        2. Cricket stadium(charges=2000)
        3. BBQ scene (charges=500)
        4. To complete your package''')
# applying loop for overall conditions
    while True:
        # applying loop for taking entertainment choices
        while True:
            entertain = int(input("Enter Your Choice You want to add in your program: "))
            if entertain in range(1, 5):
                break
            else:
                print("Please Enter Correct Choice from 1,4")

        # Handle user's choice for entertainment options
        if entertain == 1:
            days = int(input("Enter How many times you want to enjoy Qawwali nights?:"))
            amount = qawwali * days
            expense.append(amount)
            print()
            print(f"{name}, the charges for Qawwali nights are ['{amount}'] Pkr")
            print()

        elif entertain == 2:
            days = int(input("Enter How many times you want to enjoy Cricket scenes?:"))
            amount = cricket * days
            expense.append(amount)
            print()
            print(f"{name}, the charges for Cricket nights are ['{amount}'] Pkr")
            print()

        elif entertain == 3:
            days = int(input("Enter How many times you want to enjoy BBQ scenes?:"))
            amount = bbq * days
            expense.append(amount)
            print()
            print(f"{name}, the charges for BBQ nights are ['{amount}'] Pkr")
            print()

        elif entertain == 4:
            print("Thanks for upgrading your program! Hope you enjoy your trip!")
            print("Best wishes and safe travels from Raba Event Management!")
            break
        # This will go when if or elif statement are executed
        # Ask user if they want to continue adding choices
        ask = input("Do you want to continue adding choices? (y/n): ")
        if ask not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
        elif ask == "n":
            result=sum(expense)
            print(f"The Total expense of your trip is {result}")
            print("Hope you enjoy using our services")
            break
    print("Your program has been completed!")    
# checking for cruise booking    
elif choice==2:
       print(f"{name}, There is Raba cruise dinner In the town")
       print("Here are Few Details For you:")
       print("Per head charges of cruise==5000")
       print("Extra expenses are based on your choices")
       print(f"{name} We are glad to serve you! Let us know Your Requirements")
       print()
       ask=int(input("How Many members have you to join on cruise?: "))
       rent=ask*cruise
       expense.append(rent)
       print()
       print(f"Total price for The dinner on basis of member is [{rent}]")
       print()
    #    giving information for making cruise more beautiful
       print('''Here are more options that can entertain you!
        1. Concert (charges==1500)
        2. Candle light dinner (charges=2000)
        3. To complete your package''')
# applying this while loop for taking choice as long as user wants to give
       while True:      
        # apply loop for taking option by user
        while True:
            option=int(input("Enter Your Choice From [1,2,3]:"))
            if choice==1 or choice==2 or choice==3:
               break
            else:
             print("please enter correct choice")
        if option==1:
            days = int(input("Enter How many times you want to enjoy concert nights?:"))
            amount = concert * days
            expense.append(amount)
            print()
            print(f"{name}, the charges for concert nights are [{amount}] Pkr")
        elif option==2:
            days = int(input("Enter How many times you want to enjoy candle light dinner?:"))
            amount = candlelight* days
            expense.append(amount)
            print()
            print(f"{name}, the charges for concert nights are [{amount}] Pkr")
        elif option==3:
            print("Thanks for upgrading your program! Hope you enjoy your trip!")
            print("Best wishes and safe travels from Raba Event Management!")
            break
        # asking user after execution of if and elif statement that does
        # he want to continue or not it will execute after user enter any choice
        # means he will enter in if or elif statement on basis of choice
        ask=input("Do You Want to continue adding choices[y,n]:")
        if ask not  in ["y","n"]:
                print("Please Enter Correct word")
        elif ask=="n":
                result=sum(expense)
                print(f"The Total expense of your trip is ['{result}']")
                print("Hope you enjoy using our services")
                break
              
         
             
        



      




                   
               
                      


                    
               
            
            
            
                  
                   


           
               

                

              







