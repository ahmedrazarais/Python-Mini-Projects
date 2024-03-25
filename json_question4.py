# Error Handling in JSON Parsing:
# Write Python code to handle the situation when parsing the following JSON string fails due to invalid syntax:

# python
# Copy code
# json_string = '{"name": "John", "age": 30, "city": "New York"'

import json 


# using try except 
json_string = '{"name": "John", "age": 30, "city": "New York"'
try:
    parsed_string=json.loads(json_string)
except ValueError:
    print("Invalid syntax")
