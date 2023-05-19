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


# ***** Main routine goes here *****
while True:
    how_many = num_check("How many shapes would you like to calculate? ", 0, 10)

    print("You will be calculating {} shapes".format(how_many))
    print()
