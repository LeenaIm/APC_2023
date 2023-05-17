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


# Main Routine goes here...

# statement generator
statement_generator("Welcome to the Area and Perimeter Calculator", "*")
print()


def instructions():
    print()
    print("Instructions go here")
    print("Program continues...")


# If users want to see the instructions, display them
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
    instructions()

# If users do not want to see instructions, continue program
if want_instructions == "no" or want_instructions == "n":
    print("Program continues...")
