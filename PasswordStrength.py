# Certainly! Here's another interesting task:

# ### Task: Password Strength Checker

# Write a Python program that checks the strength of a password entered by the user. Assess the password based on the following criteria:

# 1. At least 8 characters long.
# 2. Contains a mix of uppercase and lowercase letters.
# 3. Includes at least one digit.
# 4. Includes at least one special character (e.g., @, #, $, etc.).

# Provide feedback to the user about the strength of their password.

# For example:
# - "Strong Password!" if it meets all criteria.
# - "Weak Password! Add more characters." if it's too short.
# - "Weak Password! Add uppercase and lowercase letters." if it lacks letter variety.

# This task will allow you to practice string manipulation, conditionals, and user input validation!



#  taking input of user:
# Taking input of user:
psd = input("Enter Your Password:")

# CONDITIONS FOR CHECKING STRENGTH OF PASSWORD:
if len(psd) >= 8 and any(c.isalpha() for c in psd) and any(c.islower() for c in psd) and any(c.isupper() for c in psd) and any(c.isdigit() for c in psd) and any(c in "@$%^&*())_+{}{}" for c in psd):
    print("STRONG PASSWORD!!")
elif len(psd) < 8:
    print("WEAK PASSWORD! ADD MORE CHARACTERS")
else:
    if not any(c.isupper() for c in psd) or not any(c.islower() for c in psd):
        print("WEAK PASSWORD! ADD UPPERCASE AND LOWERCASE PASSWORD")

      

       


