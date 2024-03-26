# Question:
# You are designing a JSON schema for a university's course registration system. Each course has the following attributes:

# Course code (a unique identifier, e.g., "COMP101")
# Course name
# Instructor (name of the instructor teaching the course)
# Credits (number of credits for the course)
# Schedule (a list of dictionaries, each representing a class session with attributes: day of the week, start time, and end time)
# Design a JSON structure to represent this schema, and provide an example JSON object for a course titled "Introduction to Computer Science" (code "COMP101"), taught by "Dr. Smith", worth 3 credits, with classes scheduled on Mondays from 9:00 AM to 10:30 AM and Wednesdays from 1:00 PM to 2:30 PM.

# Example JSON Structure:

json_data_structure={"Course_code":"PRO456","Course_name":"Programming","Instructor":"Dr Maria","Credits":5,
                     "shedule":[{"day":"sunday","start_time":"8:00 Am","ending_time":"12:00 Am"},{"day":"thursday","start_time":"9:00 Am","ending_time":"11:00 Am"}]}


# "Introduction to Computer Science" (code "COMP101"), taught by "Dr. Smith", worth 3 credits, with classes scheduled on Mondays from 9:00 AM to 10:30 AM and Wednesdays from 1:00 PM to 2:30 PM.
# JSON Structure
json_data_structure = {
    "Course_code": "COMP101",
    "Course_name": "Introduction to Computer Science",
    "Instructor": "Dr. Smith",
    "Credits": 3,
    "Schedule": [
        {"day": "Monday", "start_time": "9:00 AM", "end_time": "10:30 AM"},
        {"day": "Wednesday", "start_time": "1:00 PM", "end_time": "2:30 PM"}
    ]
}

# Extracting information from JSON
result = f"{json_data_structure['Course_name']} ({json_data_structure['Course_code']}), taught by '{json_data_structure['Instructor']}', worth {json_data_structure['Credits']} credits, with classes scheduled on: "

schedule_info = []
for session in json_data_structure['Schedule']:
    schedule_info.append(f"{session['day']} from {session['start_time']} to {session['end_time']}")

print(result + ', '.join(schedule_info))

    


