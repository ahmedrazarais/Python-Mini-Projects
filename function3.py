# 3. Write a function to input a list of integers from the user. The function returns the list to the caller.
numbers=[]
def input_numbers():
    while True:
        try:
            val=int(input("Enter NUmbers (enter 0 to terminate) :"))
            if val==0:
                break
            else:
                numbers.append(val)
        except ValueError:
            print("Invalid Input") 
    return numbers            # returniing the list
numbers=input_numbers()         # save in a variable
print(numbers)