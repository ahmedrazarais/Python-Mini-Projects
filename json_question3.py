# Adding Data to JSON Array:
# Write Python code to add a new person with name "Bob" and age 35 to the following JSON array:

# json
# Copy code
# [{"name": "Alice", "age": 25}, {"name": "Charlie", "age": 40}]

import json

given_array=[{"name": "Alice", "age": 25}, {"name": "Charlie", "age": 40}]

# setting json_file_pith
file_path="Python-Mini-Projects/working.json"

# first writting that data in json file

with open(file_path,"w") as file:
    json.dump(given_array,file)
    print(" Given Data has been written successfully")

# reading data from json file
    
with open(file_path) as reading:
    contents=json.load(reading)


# now updatae data in json file name "Bob" and age 35
new_data={"name":"Bob","age":35}
contents.append(new_data)

# write updated data in json file
with open(file_path,"w") as modification:
    json.dump(contents,modification)
    print("Modified data is write bak to file")
    
