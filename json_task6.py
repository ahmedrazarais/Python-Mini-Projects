# Removing Key from JSON Object:
# Write Python code to remove the key "age" from the following JSON object:


# {"name": "John", "age": 30, "city": "New York"}


import json

data={"name": "John", "age": 30, "city": "New York"}
# setting json_file_pith
file_path="Python-Mini-Projects/working.json"

# first writting that data in json file

with open(file_path,"w") as file:
    json.dump(data,file)
    print(" Given Data has been written successfully")

# now reading data from json file

with open(file_path) as reading:
    extraced_data=json.load(reading)

# now do modification
del extraced_data["age"]

# write back modified data
with open(file_path,"w") as file:
    json.dump(extraced_data,file)
    print(" MOdified Data has been written successfully")


