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


# Asks user how many shapes to calculate, must be more (or equal) to 1 and less than (or equal) to 10
shape_amount = num_check("How many shapes to calculate? ",
                         "Please enter an integer more than (or equal) to 1 and less than (or equal) to 10\n",
                         int)

print("You will be calculating {} shape/s".format(shape_amount))
print()
