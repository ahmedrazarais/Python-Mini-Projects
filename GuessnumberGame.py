import random   # import random

def number_game():      # making a function
    print("Welcome To Number Guessing Game!!")
    guess_number=random.randint(1,100)     # generate btw 1 100
    user_try=0   # initial user try ==0
    while True:        # applying loop to take multiple try
        try:              # using try except to avoid conflicts

            #Taking user input
            num_Ask=int(input("Enter Guess Number (enter 0 to exit from game) :"))
            # exit the game on certain condition
            if num_Ask==0:
                print("Game Is exiting...")
                return
            # giving user hint on certain conditions
            if num_Ask>guess_number:
                print("Your Guess Number Is High!!")
                user_try+=1
            elif num_Ask<guess_number:
                print("Your Guess Number Is  low")
                user_try+=1       # increment user try on evey try
            elif num_Ask==guess_number:
                print("Congratulations You win the game!!")
                user_try+=1
                print(f"You Total take {user_try} attempts to win the Game")
                return     # when user win the game
        except ValueError:        
            print("Please Enter a valid Number")
number_game()     # calling the function