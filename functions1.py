# 1. Write a function to count and return negative values in a list. The list is passed as argument to the function.
my_list=[]      #making an empty list
neg_list=[]        # making list for negative numbers
def neg_count(my_list):      #defining function 
        print("Enter Numbers as much as you want enter 0 to terminate")
        while True:            # apply loop for taking input 
         try:               # use try except to prevent 
           numbers=int(input("Enter Numbers :"))
           if numbers==0:
              break
           else:
              my_list.append(numbers)      # appending values in list
         except ValueError:
             print("Invalid Input ")
        count=0
        for i in my_list:                   # checking negative count
             if i<0:
                  count+=1
                  neg_list.append(i)
        print(f"Total Negative Numbers Are {count} and ther are {neg_list}")
                 
neg_count(my_list)       # calling the function
print(f"Your Entered List Is : {my_list}")      # printing list      




