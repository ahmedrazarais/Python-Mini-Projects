# MAKING A CAR GAME 
print(''' Hey There Is A Start Of Car game
 Type "help" For Any Infomation!

 PLEASE WAIT!
 GAME LOADING....''')
# APPLying loop for starting the game 
while True:
    word=input('Enter the word "ready" For Instructions:') 
    word_lower=word.lower()
    if word_lower in "ready":
        # printing instructions
        print("START--TO start The Car")
        print("Stop --TO stop The Car")
        print("Quit--TO exit The game")
        break
    else:
        print("I dont understand what you mean")
# APPLYING LOOP FOR CHOICES        
# initiliazing started and stopped to False
started=False
stopped=False
while True:
    choice=input('Write choice (start,stop,quit) To start The Game:')        
    choice_lower=choice.lower()
    if choice_lower=="start":
        if started:
            print("Car has already Started!")
        else:    
            started=True
            print("Car Started and ready to go!...")
    elif choice_lower=="stop":
        if stopped:
            print("Car already stopped !")
        else:
           stopped=True    
           print("Car Stopped ")    
    elif choice_lower=="quit":
        print("Game Over")    
        break
    else:
        print("Please Enter Correct options[start,stop,quit] ")


   




