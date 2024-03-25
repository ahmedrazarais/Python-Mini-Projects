# Parsing JSON in Python:
# Write Python code to parse the following JSON string and
# {"name": "John", "age": 30, "city": "New York"}

import json

# JSON string to parse
data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse the JSON string
parsed_data = json.loads(data)

# Print the value associated with the key "age"
print("Age:", parsed_data["age"])

# setting json file path
json_path = "Python-Mini-Projects/working.json"

# Write the parsed data to a JSON file
with open(json_path, "w") as file:
    json.dump(parsed_data, file)
    print("Data has been successfully added to the file.")









