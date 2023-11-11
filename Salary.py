# 13. Write a Python program to input basic salary of an employee. It calculates and prints the gross and net salary
# according to following rules.
# Gross Salary = Basic Salary (BS) + House Rent Allowance (HRA) + Dearness Allowance (DA)
# Net Salary = Gross Salary (GS) – Deductions (DD)
# BS <= 10000 : HRA = 20% of BS, DA = 80% of BS, DD = 2% of BS
# BS <= 20000 : HRA = 25% of BS, DA = 90% of BS, DD = 4% of BS
# BS > 20000 : HRA = 30% of BS, DA = 95% of BS, DD = 10% of BS

# 100
# Percentage×Amount​
 


# TAKING INPUT BY USER OF BASIC SALARY:
BS=int(input("Enter Your Basic Salary:"))
# calulating HRA:
if BS<=10000:
    HRA=(0.20*BS)
    DA=(0.8*BS)
    DD=(0.02*BS)
elif BS<=20000:
    HRA=(0.25*BS)
    DA=(0.90*BS)
    DD=(0.04*BS)
elif BS>20000:
    HRA=(0.30*BS)
    DA=(0.95*BS)
    DD=(0.10*BS)
else:
    print()    
# CALCULATING GROSS SALARY:
gross_salary=BS+HRA+DA
# CALCULATING NET SALARY
net_salary=gross_salary-DD
# PRINTING BASIC ,GROSS,NET SALARY 
print(f"Your Basic salary is::{BS}\nYour Gross salary is::{gross_salary}\nYour Net Salary is::{net_salary}")