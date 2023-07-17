import math
import pandas


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


# if response is yes/y, function returns yes
# if response no/n, function returns no
# prints error message and asks question again if response is neither yes or no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")
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
- If you enter triangle, the calculator will ask you for the base length, the height and the side lengths 
- If you enter circle, the calculator will ask you for the radius

At the end of your use with the Area & Perimeter calculator, a history will be printed out with your shapes and 
their Area & Perimeter.

**** Calculator launched! ****''')
    print()


# list of valid responses
yes_no_list = ["yes", "no"]
shape_list = ["triangle", "square", "circle", "rectangle"]

# statement generator
statement_generator("Welcome to the Area and Perimeter Calculator", "*")
print()

# asks user if they want to read instructions
# if yes, displays instructions
if yes_no("Do you want to read the instructions? ") == "yes":
    instructions()

# asks user how many shapes they want to calculate
# prints error message if answer is not an integer from min 1 - max 10
print()
shape_amount = num_check("How many shapes to calculate? ",
                         "Please enter an integer more than (or equal) to 1 and less than (or equal) to 10\n",
                         int)
print()
print("Let's get calculating...")
print()

# shape choice checker, asks users to choose from shape list
for shape in range(shape_amount):
    shapes = shape + 1
    choose_instruction = "Please choose from square (s), rectangle (r), triangle (t) or circle (c): "

    heading = "Shape {} of {}".format(shapes, shape_amount)

    print(heading)
    choose_error = "Error! Please choose a shape from the options..."
    user_choice = choice_checker(choose_instruction, shape_list, choose_error)
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
        area = length ** 2

        # calculate square perimeter
        perimeter = length * 4

        print()
        print("The area of the {} is: {}".format(user_choice, area))
        print("The perimeter of the {} is: {}".format(user_choice, perimeter))
        print()

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
        area = length * width

        # calculates rectangle perimeter
        perimeter = 2 * (length + width)

        print()
        print("The area of the rectangle is {}".format(area))
        print("The perimeter of the rectangle is {}".format(perimeter))
        print()

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
        area = math.pi * radius ** 2

        # calculate circle perimeter
        circumference = 2 * math.pi * radius

        print()
        print("The area of the circle is: {}".format(area))
        print("The perimeter of the circle is: {}".format(circumference))
        print()

    # if user chooses triangle, asks for base and height to calculate the area and perimeter
    # print error message if user does not enter number for base and height
    # print error message if user does not enter positive value for base and height
    # repeats question
    if user_choice == "triangle":
        valid_input = False
        while not valid_input:
            try:
                base = float(input("Enter the base of the triangle: "))
                if base <= 0:
                    print("Error! Please enter a positive value for base.")
                    print()
                    continue
                height = float(input("Enter the height of the triangle: "))
                if height <= 0:
                    print("Error! Please enter a positive value for height.")
                    print()
                    continue
                print()
                sideA = float(input("Enter side A of the triangle: "))
                if sideA <= 0:
                    print("Error! Please enter a positive value for side A.")
                    print()
                sideB = float(input("Enter side B of the triangle: "))
                if sideB <= 0:
                    print("Error! Please enter a positive value for side B.")
                    print()
                sideC = float(input("Enter the side C of the triangle: "))
                if sideC <= 0:
                    print("Error! Please enter a positive value for side C.")
                    print()
                valid_input = True
            except ValueError:
                print("Error! Please enter a number for the base and height.")
                print()

        # calculate triangle area
        area = 0.5 * base * height

        # calculate triangle perimeter
        perimeter = sideA + sideB + sideC

        print()
        print("The area of the triangle is: {}".format(area))
        print("The perimeter of the triangle is: {}".format(perimeter))
        print()
