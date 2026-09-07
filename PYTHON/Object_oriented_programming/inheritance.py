class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_vehicle(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def show_car(self):
        print(f"Model: {self.model}")


car1 = Car("Toyota", 2022, "Corolla")

car1.show_vehicle()
car1.show_car()

class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def describe(self):
        print(f"This is a {self.shape_name}")

    def display_info(self):
        print("------------------------")
        print(f"Shape: {self.shape_name}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print("------------------------")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(shape_name="Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


r1 = Rectangle(length=15, width=8)

print("Shape name:", r1.shape_name)
print("Area:", r1.area())

r1.describe()
r1.display_info()