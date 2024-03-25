# Accessing Nested JSON Data:
# Given the following JSON data representing a nested structure, write Python code to access the value of the key "email":


# {
#     "name": "Alice",
#     "age": 25,
#     "contact": {
#         "email": "alice@example.com",
#         "phone": "123-456-7890"
#     }
# }

import json

# Given JSON data representing a nested structure
given_data = {
    "name": "Alice",
    "age": 25,
    "contact": {
        "email": "alice@example.com",
        "phone": "123-456-7890"
    }
}

# Write the given data to a JSON file
json_path = "Python-Mini-Projects/working.json"
with open(json_path, "w") as file:
    json.dump(given_data, file)
    print("Data has been written successfully.")

# Access the value of the key "email"
email = given_data["contact"]["email"]
print("Email:", email)
