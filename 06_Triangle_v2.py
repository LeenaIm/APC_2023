import math
import pandas


def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


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


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = " {} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response < 1 or response > 10:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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
    choose_error = "Please choose a shape from the options above"
    user_choice = choice_checker(choose_instruction, shape_list, choose_error)
    print()
    # prints user choice
    print("Your shape is: {}".format(user_choice))
    print()

    if user_choice == "triangle":
        valid_input = False
        while not valid_input:
            try:
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                if base <= 0 or height <= 0:
                    print("Error! Please enter a positive value for base and height.")
                    print()
                    continue  # Repeat the loop if input is invalid
                print()
                sideA = float(input("Enter side A of the triangle: "))
                sideB = float(input("Enter side B of the triangle: "))
                sideC = float(input("Enter the side C of the triangle: "))
                valid_input = True
            except ValueError:
                print("Error! Please enter a number for the base and height.")
                print()
