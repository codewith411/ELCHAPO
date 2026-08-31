"""
Decorators allow us to add extra behavior
to a function without changing the original function.
"""


def my_deco(func):
    def wrapper():
        print("Starting the function...")
        func()
        print("Function has finished.")

    return wrapper


def hello():
    print("Hello World")


@my_deco
def morning_hello():
    print("Good morning!")


morning_hello()