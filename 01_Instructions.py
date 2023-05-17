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


# Instructions - how to play game
def instructions():
    print("Instructions go here")
    print("Program continues...")


# If users want to see the instructions, display them
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
    instructions()

# If users do not want to see instructions, continue program
if want_instructions == "no" or want_instructions == "n":
    print("Program continues...")
