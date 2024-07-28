class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
person = Person(name, age)
person.display_info()