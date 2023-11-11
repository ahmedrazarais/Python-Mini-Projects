# Task: Movie Recommender
# Write a Python program that recommends a movie based on the user's mood. Here's how you can structure it:
# If the user is "happy," recommend a comedy movie.
# If the user is "sad," recommend a drama or heartfelt movie.
# If the user is "excited," recommend an action or adventure movie.
# If the user is "stressed," recommend an motivational or ispirational movie.

# APPLYING LOOP FOR TAKING  CORRECT INPUT OF USER'S MOOD:
while True:
    mood=input("Enter your Current Mood:")
    if mood.lower() in ["happy","sad","excited","stressed"]:
        break
    else:
        print("Please,Enter Correct mood")
    #CONDITIONS FOR TELLING MOVIES:
if mood.lower()=="happy":
    print('You Should Watch "FINDING NEMO"')
elif mood.lower()=="sad":
    print('You Should Watch "LIFE IS BEAUTIFUL"')
elif mood.lower()=="excited":
    print('You Should Watch "THE JUMANJI"') 
elif mood.lower()=="stressed":
    print('You Should Watch "DEADS POETS SOCIETY"')      
else:
    print()      
        