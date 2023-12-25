# MAKING ALIBRARY CATALOG FOR USER IN WHICH HE ADD NAME OF BOOK TITLE AND PUBLISH YEAR 
# AFTER EVERY ADDITION YOU MUST ASK USER IF HE WANT TO ADD MORRE OR NOT IF HE SAY YES 
# GIVE HIM CHANCE TO DO THAT IF HE SAY NO THEN YOU SHOULD GIVE USER THREE OPTION 
# SEARCH,UPDATE OR DELETE IF USER WANT TO SAERCH THE BOOK THEN ASK HIM TITLE OF BOOK 
# AND THEN DISPLAY IT IF HE WANT TO DELETE THE BOOK DO SAME ASK TITLE AND THEN DELETE THAT BOOK IF USER WANTS 
# TO UPDATE SO GIVE HIM JUST ONE OPTION THAT HE IS ABLE TO UPDATE PUBLISH YEAR BY GIVVING TITLE OF book
# # THEN IF USER WANTS TO END THE PROGRAM END IT BY PRINTING THE LIBRARY OF USER
print("\tLIBRARY MANAGEMENT")      #printing details to user
print("""There Is An Application Designed For You Where There Are So Many Flexiblities For You:        
      1. Add book
      2. Update book
      3. Delete Movie
      4. Search The Movie
      5. Save The Data In File""")
library=[]            #MAKING AN EMPTY LIST
while True:         #APPLY LOOP FOR TAKING USER INPUT FOR ADDING BOOKS
    book=input("Enter Book Name:")
    title=input("Enter Title Of Book:")
    year=input("Enter Year of Publish:")
    ask=input("Did You Want to enter More Books?[yes/no]:")
    ask=ask.lower()             #CONVERTING IN LOWER
    if ask=="no":          
        lib={"name":book,"title":title,"year":year}
        library.append(lib)
        print("your Library is:")
        print()
        for check in library:
         for key,value in check.items():
            print(f"{key}:{value}")
         print()
        break
    else:
        print("Alright! Add more books...")
        lib={"name":book,"title":title,"year":year}
        library.append(lib)
        print("Your Library catalog is:")
        print()
        for check in library:
         for key,value in check.items():
            print(f"{key}:{value}")
         print()
while True:   # APPLY THIS LOOP FOR REMAINING CONDITION SEARCH UPDATE AND SO ON
          while True:            #APPLY THIS LOOP TO MAKE SURE USER ENTER CORRECT CHOOICE
            choice=input("Enter Your Choice [update/search/delete/end/save]:")
            choice=choice.lower()
            if choice=="update" or choice=="delete" or choice=="search" or choice=="end" or choice=="save":       
              break
            else:
             print("Something went wrong you might enter wrong keyword")   
            #  found=False
          if choice=="search":      #APPLY CONDITION FOR SEARCH
            fix="title"
            user_title=input("Enter The Title of book to search:")
            user_title=user_title.lower()
            lib={"name":book,"title":title,"year":year}
            found=False
            for check in library:             
              if check.get("title") == user_title:
               found=True
               if found:
                    print(f"Name Of Book: {check.get("name")}")
                    print(f"Title Of Book: {check.get("title")}")
                    print(f"Year Of Publish: {check.get("year")}")
            if not found:
                  print(f"There Is no Book of this title {user_title}")
          elif choice=="update":         #APPLY CONDITION FOR UPDATE
           fix="title"
           lib={"name":book,"title":title,"year":year}
           library
           ask=input("Enter Title of book:")
           year=input("Write The year what you want to write in replacement:")
           found=False      
           for check in library:
                if check.get(fix)==ask:
                 check.update({"year":year})
                 found=True
                 if found:
                    print("Your updated library is:")
                    for check in library:
                      for key,value in check.items():
                       print(f"{key}:{value}")
                      print()      
           if not found:
              print("You Make some mistake check title of books")                     
          elif choice=="delete":          #APPLY CONDITION FOR DELETE
             fix="title"
             user=input("Enter Title of the book to delete the book:")
             found=False
             for check in library:
                if check.get(fix)==user:
                   del check["name"]
                   del check["title"]
                   del check["year"]
                   found=True
                   print("Book Is deleted from library")
                   print("Your Updated library is:")
                   if found:
                       for check in library:
                        for key,value in check.items():
                         print(f"{key}:{value}")
                        print()                      
             if not found:
              print("You Enter Wrong Title of book")          
          elif choice=="save":
              if not library:
               print("No Data To Save")     
              else:
               file_name=input("Enter File Name With Path:") # asking file name from user
               with open (file_name,"w+") as file:     #open in write and read mode
                file.write("Details Of Library:\n")
                for check in library:
                 for key,value in check.items():
                    result=(f"{key}:{value}\n") 
                    file.write(result)        # writting in file
                file.seek(0)          # seek to move cursor to start
                print(file.read())     # read afile
             



          elif choice=="end":
           print("App has been closed")
           print("Your complete libraray after that is:")
           print() 
           for check in library:
              for key,value in check.items():
                 print(f"{key},{value}")
              print()
              break
           break            #BREAKING THE LOOP
   
                 
     
                
             

                 
        



