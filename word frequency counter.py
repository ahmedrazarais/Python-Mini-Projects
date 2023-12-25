# Task: Word Frequency Counter

# Create a Python script that reads a text file, counts the frequency of each word in the file, and then writes the word frequencies to another text file. Follow these steps:
# Input File:
# Choose or create a text file (input.txt) with a reasonable amount of text.
# Word Frequency Counter:
# Read the contents of the input file.
# Tokenize the text into words (ignoring punctuation and converting to lowercase).
# Count the frequency of each unique word.
# Output File:
# Write the word frequencies to an output text file (output.txt).
# Each line in the output file should contain a word and its corresponding frequency.
# User Interaction:
# Allow the user to input the file path for the input text file.
# Additional Challenge (Optional):
# Exclude common words (stop words) like "the," "and," "is," etc., from the word frequency count.
# Display the top N most frequent words.


# print("\t WORD FREQUENCY COUNTER")
# user_source_file=input("Enter Source File Name With Path:")     # taking user input of source file
# if not user_source_file:
#     print("No Data In A File")
# else:
#   try:
#     with open(user_source_file) as file:            #use with so file automatically closed
#      result=file.read()       # read afile

#      result=result.split()        # splitting on spaces
#      stop_words=["the", "is", ","]
#      new = [i for i in result if i not in stop_words]   #listcomprehension for removing specific words                                  

#      final={}                                #empty dictionary
#      for word in new:                        #loop on list
#         occurence=new.count(word)           #using list mehtod to count occurence
#         occurence=str(occurence)
#         words=word
#         final.update({word:occurence})      # updating the word with its total occurence        
#      print("Maximum frequency Word is:")
#      max_key = max(final, key=lambda k: int(final[k]))      # printing word with highest frequency
#      print(f"The key with the maximum value is: {max_key}")
#      user_dest_file=input("Enter Destination File Name With Path:")     # taking user input
#      with open (user_dest_file,"w+") as new:
#       for key,value in final.items():       #loop on key pair of dictionary
#        answer=(f"{key}:{value}")    
#        new.write(f"{answer}\n")            #writting in destination file
#      new.seek(0)                             # seek to move cursor to start
#      print(new.read())                    
#   except FileNotFoundError:
#      print("File Not Found You Entered Wrong Path")   


print("\t WORD FREQUENCY COUNTER")

user_source_file = input("Enter Source File Name With Path:")

if not user_source_file:
    print("No Data In A File")
else:
    try:
        with open(user_source_file) as file:
            result = file.read()  # read a file
            result = result.split()  # splitting on spaces
            stop_words = ["the", "is", ","]
            new = [i for i in result if i not in stop_words]  # list comprehension for removing specific words

            final = {}  # empty dictionary
            for word in new:  # loop on list
                occurrence = new.count(word)  # using list method to count occurrence
                occurrence = str(occurrence)
                final.update({word: occurrence})  # updating the word with its total occurrence
            print("Maximum frequency Word is:")
            if final:
             max_key = max(final, key=lambda k: int(final[k]))  # printing word with the highest frequency
             print(f"The key with the maximum value is: {max_key}")
            else:
                print("No Words Entered")

            user_dest_file = input("Enter Destination File Name With Path:")  # taking user input

            with open(user_dest_file, "w+") as new:
                for key, value in final.items():  # loop on key pair of dictionary
                    answer = (f"{key}:{value}")
                    new.write(f"{answer}\n")  # writing in the destination file
                new.seek(0)  # seek to move the cursor to the start
                print(new.read())

    except FileNotFoundError:
        print("File Not Found. You Entered the Wrong Path")
  
