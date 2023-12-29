
# 2. Write code that inputs a list and a value. If the value is present in the list it returns the index of its first occurrence,

user_list=[]
def index(user_list):
    try:
      target_value=int(input("Enter  targeted Value to check index:"))
    except ValueError:
        print("Invalid Input")
    while True:
        try:
            num=int(input("Enter Numbers (enter 0 to terminate) :"))
            if num==0:
                break
            else:
                user_list.append(num)
        except ValueError:
            print("Invalid Input")
    if target_value in user_list:
        z=user_list.index(target_value)
        print(f"The {target_value} is found at index {z}")
    else:
        print("Value Is not found")
index(user_list)
print(f"You Entered The List : {user_list}")