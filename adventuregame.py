# Task: Adventure Game
# Write a Python program that simulates a text-based adventure game. Create a scenario with different choices and outcomes. Here's a simple example to get you started:

# The user starts in a mysterious forest.
# Prompt the user with choices like "Go left," "Go right," or "Stay put."
# Based on the user's choice, reveal different outcomes and prompt them with more choices.
# Create at least three different possible endings for the adventure.
# For example:

# If the user chooses to go left, they might find a hidden treasure.
# If the user chooses to go right, they might encounter a friendly creature.
# If the user chooses to stay put, they might discover a magical portal.
# Use if-else statements to handle the different choices and outcomes. You can make the adventure as simple or as complex as you like!

# This task will allow you to practice conditional statements in a fun and creative way. Enjoy building your adventure game!


# starting the game:
name=input("Enter Your Name:")
print(f"Good Evening {name} Let's start the game...")
print("You are now in a mysterious forest")
print("You have a choice to GO LEFT")
print("You have a choice to GO RIGHT")
print("You have a choice to STAY PUT")
# APPLYING LOOP FOR TAKING CORRECT INPUT:
while True:
    choice=input("Enter your choice (go left , go right , stay put):")
    if choice.lower() in ["go left" , "go right" , "stay put"]:
        break
    else:
        print("Enter Appropiate Choice")
# CONDITIONS FOR GAME:
if choice.lower()=="go left":
    print("YOU FIND A HIDDEN TRAESURE")
elif choice.lower()=="go right":
    print("YOU FIND A FRIENDLY CULTURE")
elif choice.lower()=="stay put":
    print("YOU DISCOVER A MAGICAL PORTAL")
else:
    print("GAME OVER")        
