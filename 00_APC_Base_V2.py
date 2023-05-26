# checks user response is yes / no
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


# Functions go here
# Number checker (asks user for an integer, minimum is 1 maximum is 10)
# Displays error message if response is less than 1 or more than 10)
def num_check(question, error, num_type):
    valid = False
    error = "Please enter an integer more than (or equal) to 1 and less than (or equal) to 10\n"
    while not valid:

        try:
            response = num_type(input(question))

            if response < 1 or response > 10:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine goes here...

# Introduction statement generator
statement_generator("Welcome to the Area and Perimeter Calculator", "*")
print()


def instructions():
    print()
    print("Instructions go here")
    print()


# If users want to see the instructions, display them
want_instructions = yes_no("Do you want to read the instructions? ")

# If users want to see instructions, show them and continue program
if want_instructions == "yes":
    instructions()

# If users do not want to see instructions, continue program
if want_instructions == "no":
    print()

# Asks user how many shapes to calculate, must be more (or equal) to 1 and less than (or equal) to 10
shape_amount = num_check("How many shapes to calculate? ",
                         "Please enter an integer more than (or equal) to 1 and less than (or equal) to 10\n",
                         int)

print("You will be calculating {} shape/s".format(shape_amount))
print()
