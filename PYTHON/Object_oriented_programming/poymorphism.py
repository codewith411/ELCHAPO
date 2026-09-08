class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def area(self):
        print("Area calculation not available")

    def describe(self):
        print(f"This is a {self.shape_name}")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.shape_name = "Square"


# Create objects
r1 = Rectangle(20, 12)
t1 = Triangle(10, 8)
s1 = Square(6)


# Polymorphism
shapes = [r1, t1, s1]

for shape in shapes:
    print(shape.shape_name)
    print("Area:", shape.area())
    shape.describe()
    print("----------------")