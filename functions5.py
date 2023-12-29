
# 5. Write a function which takes as input a file name and a list of values and write the list of values to the specified file. If
# the file already exists then the new values are appended to it.
file_name = input("Enter File Name:")

def write_to_file(file_name, result):
    try:
        while True:
            number = int(input("Enter Numbers (enter 0 to terminate): "))
            if number == 0:
                break
            else:
                result.append(number)

        # Open the file in append mode and write the numbers
        with open(file_name, "a") as file:
            for i in result:
                file.write(f"{i} ")
            file.write("\n")
    except ValueError:
        print("Invalid Input")

# Initialize an empty list to store numbers
result = []

# Call the function to get input and write to the file
write_to_file(file_name, result)

# Read and print the entire file content after writing
with open(file_name, "r") as file:
    content = file.read()
    print(content)