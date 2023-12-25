# Task: Movie Database Manager
# Create a simple movie database manager in Python. The program should allow users to:
# Add a Movie:
# Prompt the user to enter details about a movie (title, genre, release year, director, etc.).
# Store the movie information in a data structure of your choice (e.g., a list of dictionaries).
# Display Movies:
# Display a list of all movies with their details.
# Search for a Movie:
# Prompt the user to enter a movie title.
# If the movie is in the database, display its details; otherwise, show a message that the movie is not found.
# Update Movie Details:
# Allow the user to update details (e.g., change the director or release year) of a specific movie.
# Delete a Movie:
# Allow the user to delete a movie from the database.
# Save/Load Movies to/from a File:
# Implement a way to save the current movie database to a file and load it back when the program starts.

print("\tMOVIE DATABASE MANAGEMENT")      #printing details to user
print("""There Is An Application Designed For You Where There Are So Many Flexiblities For You:        
      1. Add Movie
      2. Update Movie
      3. Delete Movie
      4. Display Movie
      5. Search The Movie
      6. Save The Data In File""")

main=[]                 # making an empty list
while True:                      #applying loop for overall conditions
    while True:                 # applying loop for taking user choice
        choice=input("Enter Your Choice add , update , delete , search, save , display , end :")
        choice=choice.lower()           # converting all in lower
        if choice=="add" or choice=="update" or choice=="search" or choice=="delete" or choice=="save" or choice=="end" or choice=="display":
            break
        else:
            print("You entered wrong option please TRY AGAIN ")
    if choice=="add":           # now applying conditions
        title=input("Enter Movie Title:")
        year=input("Enter Movie Release Year:")
        director=input("Enter Movie Director's Name:")
        details={"title":title,"year":year,"director":director} #makingt adictionary
        main.append(details)       #appending in list
        print()
        for i,movie in enumerate(main):     #printing in standard format
            for key,value in movie.items():
                print(f"{key} : {value}")
            print()
    elif choice=="display":
        if not main:          # if no movie enter
            print("No Movie Data To Display")
        else:
            print("Here Is The Display Of Your Movies:")
            for i,movie in enumerate(main):          # displaying result
                for key,value in movie.items():
                    print(f"{key} : {value}")
                print()
                        
    elif choice=="delete":
        if not main:
            print("There Is No Data To Delete")
        else:
         fix="title"        #fix the title
         user_ask=input("Enter Movie title to delete that movie Complete Details:")
         found=False
         for check in main:
          if check.get(fix)==user_ask:     #if user enter value==titleget
             del check["title"]          #deleting dictionaty
             del check["year"]
             del check["director"]
             found=True
             if found:
              print("Updated View After Deleting:")
              for i,movie in enumerate(main):           #update in standard form
                for key,value in movie.items():
                    print(f"{key}:{value}")     
                print()
         if not found:            # if wrong title
              print("You Entered Wrong Title")
    elif choice=="search":
        if not main:
            print("No Movie Entered To Search")
        else:
         fix="title"
         user=input("Enter Movie Title To search The Movie:")
         found=False
         for check in main:
            if check.get(fix)==user:
                found=True
                if found:   #Printing the search movie if condition meet
                       print("Your Search Movie:")
                       print(f"Title Of Movie: {check.get("title")}")   
                       print(f"Release Year: {check.get("year")}")   
                       print(f"Director Of Movie: {check.get("director")}")
         if not found:
            print("You Entered Wrong Title Of movie")
    elif choice=="update":
        if not main:
            print("You First Entered Movie Then Update it")
        else:
         details={"title":title,"year":year,"director":director}
         fix="title"
         user_ask=input("Enter Title Of Movie You Want To Update:")
         found=False
         for check in main:
            if check.get(fix)==user_ask:
                found=True
                if found:
                    #asking that what he want to update then applying conditions seperately for each
                    ask=input("Enter What you want to update:?").lower()          
                    if ask=="title":
                        new_tit=input("Enter The New Title:")
                        check.update({"title":new_tit})
                        for i,movie in enumerate(main):
                            for key,value in movie.items():
                                print(f"{key}:{value}")
                            print()
                    elif ask=="year":
                         new_year=input("Enter The New Year:")
                         check.update({"year":new_year})
                         for i,movie in enumerate(main):
                            for key,value in movie.items():
                                print(f"{key}:{value}")
                            print()
                    elif ask=="director":
                         new_dir=input("Enter The New Director Name:")
                         check.update({"director":new_dir})
                         for i,movie in enumerate(main):
                            for key,value in movie.items():
                                print(f"{key}:{value}")
                            print()
                    else:
                        print("you Entered Wrong Keyword!!")            
         if not found:
            print(f"There Is No Movie Of That Title Name {user_ask}")
    elif choice=="save":
        if not main:
            print("No Data To Save")     
        else:
            file_name=input("Enter File Name With Path:") # asking file name from user
            with open (file_name,"w+") as file:     #open in write and read mode
             file.write("Details Of Movie:\n")
             for check in main:
                for key,value in check.items():
                    result=(f"{key}:{value}\n") 
                    file.write(result)        # writting in file
             file.seek(0)          # seek to move cursor to start
             print(file.read())     # read afile
    elif choice=="end":
        if not main:
            print("No Data Entered")
        else:
          print("Your Complete Response Is:")
          print()
          for movie in main:            # printing final response
            for key,value in movie.items():
             print(f"{key}:{value}")
            print()
        break      # breaking out of program

            
