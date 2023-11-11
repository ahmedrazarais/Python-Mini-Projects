# TAKING INPUT BY USER OF THIER MOOD:
user_mood=input("Enter Your Mood:")
# DEFINNG EMOJIS:
emojis = {
    'happy': '😊',
    'sad': '😢',
    'excited': '🎉',
    'angry': '😡',
    'ego': '😤',
    
}
# CONDITIONS:
if user_mood.lower() in emojis:
    print(f"Your mood is  {user_mood} :{emojis[user_mood.lower()]}")
else:
    print(f"your mood is not preductable :😐")    

