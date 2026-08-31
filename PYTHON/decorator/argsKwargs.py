# *args and **kwargs in a decorator
# This decorator prints information about a function
# whenever the function is called.


def log_deco(func):

    def wrapper(*args, **kwargs):
        print("----------------------------------------")
        print("Args:", args)
        print("Kwargs:", kwargs)

        result = func(*args, **kwargs)

        print(f"Function called was: {func.__name__}")
        print("Result:", result)
        print("----------------------------------------")

        return result

    return wrapper


@log_deco
def greet():
    print("Hello World")
    return "Greeting completed"


@log_deco
def add(a, b):
    return a + b


@log_deco
def introduce(name, age):
    return f"My name is {name} and I am {age} years old"


# No arguments
greet()

# Positional arguments
add(10, 20)

# Keyword arguments
add(a=30, b=40)

# Keyword arguments with a different function
introduce(name="Alex", age=25)