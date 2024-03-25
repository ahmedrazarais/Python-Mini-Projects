# Updating JSON Data:
# Given the following JSON object, update the value of the key "city" to "Chicago":

# json
# Copy code
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
    
extraced_data["city"]="Chicago"

# write modified data back to file
with open(file_path,"w") as file:
    json.dump(extraced_data,file)
    print(" MOdified Data has been written successfully")
