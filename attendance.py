# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
print("Enter Your 6 Digit Roll Number for checking attendance:")
while True:
    psd=int(input("Enter Your 6 Digit Roll-No:"))
    if 000000<=psd<999999:
        break
    else:
        print("Please Enter Appropiate Roll-No")
# PROVIDING NFORMATION ABOUT ATTENDANCE:
print("YOUR ATTENDANCE PERCENTAGE SHOULD BE ATLEAST 75% OR ABOVE!")
# APPLYING LOOP FOR TAKING INPUT:
while True:
    class_held=(input("Enter Total No. Of Classes  That Held:"))
    class_taken=(input("Enter Classes You Taken:"))
    # APPLYING CONDITON THAT USER SHOULD WRITE IN DIGIT FORM:
    if class_held.isdigit() and class_taken.isdigit():
        # CHANGING VALUES INTO INTEGER FOR CALCULATIONS
        class_held=int(class_held)
        class_taken=int(class_taken)
        break
    else:
        print("Please Write In Digit Form (E.g:(56,87))")
# CALCULATING ATTENDACE PERCENTAGE:        
attendance_per=(class_taken/class_held)*100        
# ROUNDING PERCENTAGE
attendance_per=round(attendance_per)
# PRINTING ATTENDANCE PERCENTAGE:
print(f"Your Attendance Percentage is {attendance_per}%")
# CONDITIONS FOR SITTIG IN EXAM:
if attendance_per>=75:
    print("You are Eligible to sit in exam! ")
else:
    print("You Are Not Eligible Due To Short Attendance!")    


