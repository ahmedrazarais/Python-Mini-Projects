# Working with JSON Arrays:
# Write a Python function to calculate the total quantity of fruits in the following JSON array:

# json
# Copy code


array= [{"name": "apple", "quantity": 10}, {"name": "banana", "quantity": 20}, {"name": "orange", "quantity": 15}]

result=0

for dictionaries in array:
    result+=dictionaries["quantity"]

print(f"Total Quantity : {result}")
