# Making a Program for user of two choices either go to doctor clinic or buy medicine
# initials medicines variable prices
panadol=650
paracetamol=550
disprin=30
# printing details
print('''HEY there Is A medical Store and a clinic IN the Town You Just Simply Go to Website to get a help
We have doctor who facilite you told Them What You are Facing
Write Your Full Name and 4  letter Id to get registration
''')
name=input("Enter Your Full Name:")
# applying loop fr taking user password
while True:
    psd=(input("Enter Your four letter Password:"))
    if psd.isalpha() and len(psd)==4:
        break
    else:
        print("Plese enter appropiate Password Must be four letter [abcd]")

name_c=name.capitalize()        
print(f"Your Full name is {name_c} ")
print(f"Your Registration Password is : {psd} ")
print()
print("Write 'Doctor' If you want to connect with doctor!")
print("Write 'Medicine' If you want to Go to online store!")
# applying loop for taking user choice b/w doctor and medicine
while True:
   choice=input("Write [doctor/medicine] for Further Assistance:")
   choice_lower=choice.lower()
   if choice_lower == "doctor" or choice_lower =="medicine":
    break
   else:
      print("Plese Enter Correct Keyword For Help!")
# if choice is doctor applying conditions      
if choice_lower=="doctor":
   print(f'''Hello {name_c} i am here to help you
   tell me from which disease you are suffering!
   1.write Fever if you suffering from [Fever]
   2.write Flu if you suffering from [Flu]
   3.write pain if you suffering from [pain]
''')
   while True:
    option=input("Enter Your Options[Fever,flu,pain]:")
    option_lower=option.lower()
    if option_lower=="fever" or option_lower== "flu" or option_lower== "pain":
        break
    else:
        print("Please Enter Correct Disease name")         
   if option_lower=="fever":

    print(f"{name} So You Are Suffering From Fever")      
    print( "You should Go Medical Store And Buy medicine That i recommend to you")      
    print( "You should take care of yourself")      
    print( "GET WELL SOON")      
   elif option_lower=="flu":
    print(f"{name} So You Are Suffering From Flu")      
    print( "You should Go Medical Store And Buy medicine That i recommend to you")      
    print( "You should take care of yourself") 
    print( "GET WELL SOON")   
   elif option_lower=="pain":
    print(f"{name} So You Are Suffering From pain")      
    print( "You should Go Medical Store And Buy medicine That i recommend to you")     
    print( "You should take care of yourself")  
    print( "GET WELL SOON")  
# if choice is medicine applying conditions    
elif choice_lower=="medicine":
    print(f'''Welcome to medical store {name} 
select choices for what you want to buy!
1.panadol [1 syrup=650]         
2.paracetamol [1 syrup=550]
3.disprin [1 tablet=30]                   
''')
    while True:
        med_choice=input("Enter Choice [1/2/3]:")
        if med_choice=="1" or med_choice=="2" or med_choice=='3':
          break
        else:
          print("Please Enter Correct Medicine choice")
    if med_choice=="1":     
    
     print("You choose panadol")
     quantity=int(input("Entr Quantity of medicine:"))
     bill=quantity*panadol
     print(f"{name_c} your total bill is {bill}")
     print(f"{name_c} Thank you for visiting")
    elif med_choice=="2":
     print("You choose paracetamol")
     quantity=int(input("Entr Quantity of medicine:"))
     bill=quantity*paracetamol
     print(f"{name_c} your total bill is {bill}")
     print(f"{name_c} Thank you for visiting")            
    elif med_choice=="3":
     print("you choose Disprin")
     quantity=int(input("Entr Quantity of medicine:"))
     bill=quantity*disprin
     print(f"{name_c} your total bill is {bill}")
     print(f"{name_c} Thank you for visiting") 







      
   
         


        



