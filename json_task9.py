# Serializing Objects to JSON:


# Create a Python class Person with attributes name, age, and city. Write a method to_json() that returns a JSON string representing the object.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def to_json(self):
        return {"name": self.name, "age": self.age, "city": self.city}

person = Person("raza", 19, "Karachi")
json_string = person.to_json()
print(json_string)
