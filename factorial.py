# 14. Write a Python program that takes an integer from the user and finds its factorial. Print appropriate messages and the
# result. Also include the special case for printing factorial of 0.


# TAKING INPUT:
n=int(input("Enter The Value Of Integer:"))
# CHECKING IF INTEGER IS ZERO OR NEGATIVE:
if n==0:
      print(f"Factorial Of {n} Is one")
elif n<0:
      print(f"Factorial of {n} is undefined")
    #   APPLYING LOOP FOR POSITIVE INTEGERS:
else:
      total=1
      for i in range(n,0,-1):
            total=total*i
      print(f"The Factorial Of {n} Is : {total}")      

     
     
     
                  

