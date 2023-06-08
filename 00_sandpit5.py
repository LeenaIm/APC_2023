import math


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
    print()
    print("Instructions go here")


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

#
for shape in range(shape_amount):
    shapes = shape + 1
    choose_instruction = "Please choose from circle (c), triangle (t), square (s), or rectangle (r): "

    heading = "Shape {} of {}".format(shapes, shape_amount)

    print(heading)
    choose_error = "Please choose a shape from the options above!"
    user_choice = choice_checker(choose_instruction, shape_list, choose_error)
    print()

    print("You chose: {}".format(user_choice))

    if user_choice == "square" or user_choice == "rectangle":
        try:
            length = float(input("Enter the length of the {}: ".format(user_choice)))
            width = float(input("Enter the width of the {}: ".format(user_choice)))
        except ValueError:
            print("Invalid input! Please enter a numeric value for length and width.")
        else:
            area = length * width
            perimeter = 2 * (length + width)

            print()
            print("The area of the {} is: {}".format(user_choice, area))
            print("The perimeter of the {} is: {}".format(user_choice, perimeter))
