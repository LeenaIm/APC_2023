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
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = input(question)

            # exit loop if user presses enter
            if response == "":
                return None

            # convert the response to an integer
            response = int(response)

            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here...

# statement generator
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

# Ask the user for the number of shapes to calculate
how_many = num_check("How many shapes would you like to calculate? ", 0, 10)

print("You will be calculating {} shapes".format(how_many))
print()
