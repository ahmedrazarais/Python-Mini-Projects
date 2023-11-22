# 12. Write code to find average of five non-negative integers entered by the user and print average.
# 13. Repeat problem 12, now allowing user to enter a many integers as he/she wants to. The user enters a negative number
# to terminate.
# INITIALIZING TOTAL AND COUNT TO ZERO
total = 0
count = 0

while True:
  num = int(input("Enter A Non Negative Integer: "))

  # APPLYING CONDITION TO TERMINATE IF USER ENTER NEGATIVE INTEGER
  if num < 0:
    break

  total += num
  count += 1

# APPLYING CONDITION CHECK BEFORE CALCULATING AVERAGE
if count > 0:
  avg = total / count
  print(f"The total sum is: {total}")
  print(f"The total average is: {avg}")
else:
  print("No valid input provided.")


        


            


