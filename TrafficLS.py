# Making a traffic stimulator:
while True:
    colour=input("Enter the Current Traffic Colour:")
    if colour.lower() in ["red","yellow","green"]:
        break
    else:
        print("Enter the correct colour (GREEN,YELLOW,RED)")
# CONDITIONS:
if colour.lower()=="red":
    print("STOP,Gentlemen")
elif colour.lower()=="green":
    print("LET'S GO,Gentlemen")
elif colour.lower()=="yellow":
    print("SLOWDOWN,Gentlemn")
else:
    print()        
