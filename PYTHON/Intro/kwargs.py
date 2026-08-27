# Testing kwargs
#
# List of kwargs
# kwargs = dictionary
# **kwargs collects keyword arguments


def my_kwargs(**kwargs):
    print("Kwargs type is:", type(kwargs))
    print("Kwargs are:", kwargs)

    # Access a value using its key
    # print("name is:", kwargs["name"])


# Scenario 1
# a=15, b=25, c=35
# kwargs becomes:
# {"a": 15, "b": 25, "c": 35}

my_kwargs(a=15, b=25, c=35)


# Scenario 2
# Passing different keyword arguments

my_kwargs(
    username="Brian",
    email="brian@example.com",
    country="Kenya"
)


# Scenario 3
# Passing a dictionary with **

person = {
    "username": "Alice",
    "email": "alice@example.com",
    "age": 28
}

my_kwargs(**person)


# =====================================
# NORMAL ARGUMENTS VS KEYWORD ARGUMENTS
# =====================================

def rectangle_area(length, width):
    area = length * width
    print(f"Area is {area}")


# Option 1: positional arguments
rectangle_area(10, 4)


# Variables can also be used
width = 6
length = 12

# Positional arguments
rectangle_area(length, width)


# Option 2: keyword arguments
rectangle_area(width=6, length=12)


# The parameter names must match
rectangle_area(length=20, width=5)