"""
Object Oriented Programming (OOP)

OOP is a programming concept that makes work easier
by organizing data and functions into classes and objects.

Main OOP principles:

1. Encapsulation
   - Keeping data and methods/functions inside a class.

2. Abstraction
   - Hiding unnecessary implementation details.

3. Inheritance
   - One class can reuse or extend properties and
     methods from another class.

4. Polymorphism
   - Methods can behave differently in different forms.

JavaScript, Python, C++, Java, etc. support OOP.
"""


"""
Class

A class is a blueprint for creating an object.

Think of a class as an architectural drawing of a house.

CLASS  -> Blueprint
OBJECT -> Actual thing created from the blueprint
"""


# Class
# Class names should normally be capitalized.
# Fields / properties

class Car:
    wheels = 4
    doors = 4
    engine = "Petrol"
    color = ""
    owner = ""
    location = ""
    manufacturer = "Toyota"


# Create an object from the Car class

alex_car = Car()

# Access object properties using dot notation

alex_car.owner = "Alex"
alex_car.location = "Nairobi"
alex_car.color = "Blue"

print(f"Alex's Car Owner: {alex_car.owner}")
print(f"Alex's Car Location: {alex_car.location}")
print(f"Alex's Car Wheels: {alex_car.wheels}")
print(f"Alex's Car Doors: {alex_car.doors}")
print(f"Alex's Car Engine: {alex_car.engine}")
print(f"Alex's Car Color: {alex_car.color}")
print(f"Alex's Car Manufacturer: {alex_car.manufacturer}")


# Create another object from the same class

brian_car = Car()

brian_car.owner = "Brian"
brian_car.location = "Mombasa"
brian_car.color = "Black"

print(f"Brian's Car Owner: {brian_car.owner}")
print(f"Brian's Car Location: {brian_car.location}")
print(f"Brian's Car Wheels: {brian_car.wheels}")
print(f"Brian's Car Doors: {brian_car.doors}")
print(f"Brian's Car Engine: {brian_car.engine}")
print(f"Brian's Car Color: {brian_car.color}")
print(f"Brian's Car Manufacturer: {brian_car.manufacturer}")

class Student:
    name = ""
    age = 20
    course = "Software Engineering"
    year = 1
    school = "Tech University"
    location = ""


# Create an object from the Student class

student_one = Student()

# Access and change object properties using dot notation

student_one.name = "Brian"
student_one.age = 22
student_one.location = "Nairobi"

print(f"Student Name: {student_one.name}")
print(f"Student Age: {student_one.age}")
print(f"Student Course: {student_one.course}")
print(f"Student Year: {student_one.year}")
print(f"Student School: {student_one.school}")
print(f"Student Location: {student_one.location}")


# Create another object from the same class

student_two = Student()

student_two.name = "Lydia"
student_two.age = 21
student_two.location = "Kisumu"

print(f"Student Name: {student_two.name}")
print(f"Student Age: {student_two.age}")
print(f"Student Course: {student_two.course}")
print(f"Student Year: {student_two.year}")
print(f"Student School: {student_two.school}")
print(f"Student Location: {student_two.location}")