class Animals:
    def __init__(self, name, age, gender, kind):
        self.name = name
        self.age = age
        self.gender = gender
        self.kind = kind
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Kind of animals:  {self.kind}")
name = input("Enter animals name: ")
age = int(input("Enter animals age: "))
gender = input("Enter animals gender: ")
kind = input("Enter kind of animals: ")

animal = Animals(name, age, gender, kind)
animal.display_info()