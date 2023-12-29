# # 4. Write a function to input a list of integers from the user. The function receives an empty list from user.

def get_numbers(user_list):
    while True:
        try:
            num=int(input("Enter Numbers (enter 0 to terminate) :"))
            if num==0:
                break
            else:
                user_list.append(num)
        except ValueError:
            print("Invalid Input")
    return user_list        # returning the list
user_list=[]           
result=get_numbers(user_list)
print(result)