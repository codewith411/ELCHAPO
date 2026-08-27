# Tuple
#
# *args allows a function to accept any number
# of positional arguments.
#
# The arguments are stored inside a tuple.


def my_args(*args):
    print(f"Args type: {type(args)}")
    print(f"All args: {args}")
    print(f"First arg: {args[0]}")
    print("------------------------")


# Passing several positional arguments
my_args(15, 42, 73, 88)

my_args("Python", False, 56)


# ---------------------------------
# Function for rectangle area
# ---------------------------------

def rectangle_area(length, width):
    area = length * width

    print("------------------------")
    print(
        f"Rectangle with length {length} "
        f"and width {width} has an area of {area}"
    )
    print("------------------------")


rectangle_area(12, 7)


# ---------------------------------
# Function to add two numbers
# ---------------------------------

def add_numbers(a, b):
    answer = a + b
    return answer


result = add_numbers(15, 25)

print("Result:", result)


# ---------------------------------
# Using *args to add many numbers
# ---------------------------------

def add_many(*args):
    # args is a tuple
    answer = 0

    for number in args:
        print(f"Number is {number}")
        answer = answer + number

    print(f"Total is {answer}")


add_many(12, 25, 37, 41, 56, 63)