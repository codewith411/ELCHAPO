# Function to calculate the area of a circle
# def means define a function

def calculate_circle_area(radius):
    answer = 3.142 * pow(radius, 2)

    print(f"For a circle with radius {radius}, the area is {answer}")

    return


# Calling the function
calculate_circle_area(15)


# Assigning the function to another variable
new_function = calculate_circle_area


# Calling the function using the new variable
new_function(8)