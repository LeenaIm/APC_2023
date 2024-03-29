import math
import pandas


# Checks that user has entered yes / no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


# choice checker
# list of valid options
# iterates through list and if response is an item
# in the list (or the first letter of an item), the
# full item name is returned
# output error if item not in list
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# statement generator
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = " {} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# asks user question (how many shapes)
# if response is less or equal to 0 or more than 10
# prints error message if user does not enter number/number
# less or equal to 0 or more than 10
# return response for anything else
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response <= 0 or response > 10:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Instructions - how to play
def instructions():
    print('''\n
***** Instructions *****

Welcome to the Area & Perimeter Calculator!

Shapes that can be calculated: Square (s), rectangle (r), triangle (t), circle (c)

To use this calculator...

- Enter how many shapes you need to calculate (1-10 only)
- If you enter square, the calculator will ask you for the length and width
- If you enter rectangle, the calculator will ask you for the length and width
- If you enter triangle, the calculator will ask you for the base, the height and the side lengths 
- If you enter circle, the calculator will ask you for the radius

At the end of your use with the Area & Perimeter calculator, a history will be printed out with your shapes and 
their Area & Perimeter.

**** Calculator launched! ****''')
    print()


# statement generator
statement_generator("Welcome to the Area and Perimeter Calculator", "*")
print()

# list of valid responses
shape_list = ["triangle", "square", "circle", "rectangle"]

# dictionaries to hold shape details
all_shapes = []
all_dimensions = []
all_perimeters = []
all_areas = []

shape_dict = {
    "Shape": all_shapes,
    "Dimensions": all_dimensions,
    "Perimeter": all_perimeters,
    "Area": all_areas
}

# asks user if they want to read instructions
# if yes, displays instructions
# Ask user if they want to see the instructions
want_instructions = yes_no("Would you like to read the instructions? (y/n): ")
if want_instructions == "yes":
    instructions()

# asks user how many shapes they want to calculate
# prints error message if answer is not an integer from min 1 - max 10
print()
shape_amount = num_check("How many shapes to calculate? (1-10): ",
                         "Please enter an integer more than (or equal) to 1 and less than (or equal) to 10\n",
                         int)
print()
print("Let's get calculating...")
print()

# shape choice checker, asks users to choose from shape list
for shape in range(shape_amount):
    shapes = shape + 1
    choose_shape = "Please choose from square (s), rectangle (r), triangle (t) or circle (c): "

    heading = "Shape {} of {}".format(shapes, shape_amount)

    print(heading)
    choose_error = "Error! Please choose a shape from the options..."
    user_choice = choice_checker(choose_shape, shape_list, choose_error)
    print()
    # prints user choice
    print("Your shape is: {}".format(user_choice))
    print()

    # if user choice is square asks for length and width
    # print error message if user does not enter a number for length or width
    # print error message if user does not enter positive value for length or width
    # repeats question
    if user_choice == "square":
        valid_input = False
        while not valid_input:
            try:
                length = float(input("Enter the length of the square: ".format(user_choice)))
                if length <= 0:
                    print("Error! Please enter a positive value for the length.")
                    print()
                else:
                    valid_input = True
            except ValueError:
                print("Error! Please enter a number for length and width.")
                print()

        # calculate square area
        area_square = length ** 2

        # calculate square perimeter
        perimeter_square = length * 4

        # prints area and perimeter of square
        print()
        print("The area of the square is: {:.2f}".format(area_square))
        print("The perimeter of the square is: {:.2f}".format(perimeter_square))
        print()

        # add shape, dimensions, perimeter and area to list
        all_shapes.append(user_choice)
        all_dimensions.append(length)
        all_areas.append(area_square)
        all_perimeters.append(perimeter_square)

    # if user choice is rectangle, ask for length and width
    # calculates area and perimeter
    # prints error message if user does not enter length and width
    # prints error message if user does not enter positive value for length/width
    # repeats question
    if user_choice == "rectangle":
        valid_input = False
        while not valid_input:
            try:
                length = float(input("Enter the length of the rectangle: ".format(user_choice)))
                if length <= 0:
                    print("Error! Please enter a positive value for length.")
                    print()
                    continue
                width = float(input("Enter the width of the rectangle: ".format(user_choice)))
                if width <= 0:
                    print("Error! Please enter a positive value for width.")
                    print()
                    continue
                valid_input = True
            except ValueError:
                print("Error! Please enter a number for the length and width.")
                print()

        # calculates rectangle area
        area_rectangle = length * width

        # calculates rectangle perimeter
        perimeter_rectangle = 2 * (length + width)

        # prints area and perimeter of rectangle
        print()
        print("The area of the rectangle is {:.2f}".format(area_rectangle))
        print("The perimeter of the rectangle is {:.2f}".format(perimeter_rectangle))
        print()

        # add shape, dimensions, perimeter and area to list
        all_shapes.append(user_choice)
        all_dimensions.append((length, width))
        all_areas.append(area_rectangle)
        all_perimeters.append(perimeter_rectangle)

    # if user choice is circle, ask for radius
    # calculates area and perimeter
    # prints error message if user does not enter number for radius
    # prints error message if user does not enter positive value for radius
    # repeats question
    if user_choice == "circle":
        valid_input = False
        while not valid_input:
            try:
                radius = float(input("Enter the radius of the circle: ".format(user_choice)))
                if radius <= 0:
                    print("Error! Please enter a positive value for radius.")
                    print()
                else:
                    valid_input = True
            except ValueError:
                print("Error! Please enter a number for the radius.")
                print()

        # calculate circle area
        area_circle = math.pi * radius ** 2

        # calculate circle perimeter
        circumference_circle = 2 * math.pi * radius

        # prints area and perimeter of circle
        print()
        print("The circumference of the circle is: {:.2f}".format(circumference_circle))
        print("The area of the circle is: {:.2f}".format(area_circle))
        print()

        # add shape, dimensions, perimeter and area to list
        all_shapes.append(user_choice)
        all_dimensions.append(radius)
        all_areas.append(area_circle)
        all_perimeters.append(circumference_circle)

    # if user chooses triangle, asks for base and height to calculate the area and perimeter
    # print error message if user does not enter number for base and height
    # print error message if user does not enter positive value for base and height
    # repeats question
    if user_choice == "triangle":
        valid_input = False
        while not valid_input:
            try:
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                if base <= 0 or height <= 0:
                    print("Error! Please enter a positive value for base and height.")
                    print()
                    continue
                print()
                valid_input = True
            except ValueError:
                print("Error! Please enter a number for the base and height.")
                print()

        valid_input = False
        while not valid_input:
            try:
                side1 = float(input("Enter side 1 of the triangle: "))
                if side1 <= 0:
                    print("Error! Please enter a positive value for side 1.")
                    print()
                    continue
                valid_input = True
            except ValueError:
                print("Error! Please enter a number for side 1.")
                print()

        valid_input = False
        while not valid_input:
            try:
                side2 = float(input("Enter side 2 of the triangle: "))
                if side2 <= 0:
                    print("Error! Please enter a positive value for side 2.")
                    print()
                    continue
                valid_input = True
            except ValueError:
                print("Error! Please enter a number for side 2.")
                print()

        valid_input = False
        while not valid_input:
            try:
                side3 = float(input("Enter side 3 of the triangle: "))
                if side3 <= 0:
                    print("Error! Please enter a positive value for side 3.")
                    print()
                    continue
                valid_input = True
            except ValueError:
                print("Error! Please enter a number for side C.")
                print()

        # calculate triangle area
        area_triangle = 0.5 * base * height

        # calculate triangle perimeter
        perimeter_triangle = side1 + side2 + side3

        # prints area and perimeter of triangle
        print()
        print("The area of the triangle is: {:.2f}".format(area_triangle))
        print("The perimeter of the triangle is: {:.2f}".format(perimeter_triangle))
        print()

        # add shape, dimensions, perimeter and area to list
        all_shapes.append(user_choice)
        all_dimensions.append((base, height, side1, side2, side3))
        all_perimeters.append(perimeter_triangle)
        all_areas.append(area_triangle)

# create data frame from dictionary to organise information
shape_history_df = pandas.DataFrame(shape_dict)

# rounds columns to 2 decimal places
shape_history_df = shape_history_df.round(2)

# display the user's shape history using pandas DataFrame
print("\n**** Shape Calculation History ****\n")
print(shape_history_df)
