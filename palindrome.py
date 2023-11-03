# Taking input:
word=input("Enter a word for checking palindrome:")
# conditions:
if (word[0:4])==(word[::-1]):
    # ouput:
    print("The word you enter is a Palindrome")
else:
    print("Not a palindrome")    

