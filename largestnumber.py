# TAING INPUT BY USER:
num_1=int(input("Enter An Integer:"))
num_2=int(input("Enter An Integer:"))
num_3=int(input("Enter An Integer:"))
# CHECKING THE CONDITIONS FOR LARGEST NUMBER:
if num_1>num_2 and num_1>num_3:
    print(f"{num_1} Is The Largest Number among all.")
elif  num_2>num_1 and num_2>num_3:
    print(f"{num_2} Is The Largest Number among all.")
else:
    print(f"{num_3} Is The Largest Number among all.")    