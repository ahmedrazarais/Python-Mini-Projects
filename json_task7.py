# Validating JSON Data:
# Design a Python function that takes a JSON object as input and returns True if it contains keys "username" and "password", otherwise returns False.

import json

def checking_keys(json_object):
    # Check if both  keys are present
    if "username" in json_object and "password" in json_object:
        return True
    else:
        return False

# Example JSON object
json_object = {"name": "John", "age": 30, "city": "New York"}

# Test the function with the example JSON object
print(checking_keys(json_object))  # Output will be False


