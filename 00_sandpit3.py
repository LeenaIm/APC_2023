def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


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
# number checker
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


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main Routine goes here...

# List of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["triangle", "square", "circle", "rectangle"]

rounds = check_rounds()

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

# Asks user how many shapes to calculate, must be more (or equal) to 1 and less than (or equal) to 10
shape_amount = num_check("How many shapes to calculate? ",
                         "Please enter an integer more than (or equal) to 1 and less than (or equal) to 10\n",
                         int)

print("You will be calculating {} shape/s".format(shape_amount))
print()
print("Let's get started...")
print()

shapes = 0
print()
choose_instruction = "Please choose from circle (c), triangle (t), square (s) or rectangle (r)"

heading = "Shape {} of {}".format(shapes + 1, rounds)
