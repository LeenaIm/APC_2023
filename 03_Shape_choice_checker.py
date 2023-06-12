def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()

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


# list of valid responses
yes_no_list = ["yes", "no"]
shape_list = ["triangle", "square", "circle", "rectangle"]

print()
shape_amount = num_check("How many shapes to calculate? ",
                         "Please enter an integer more than (or equal) to 1 and less than (or equal) to 10\n",
                         int)

for shape in range(shape_amount):
    shapes = shape + 1
    choose_instruction = "Please choose from circle (c), triangle (t), square (s), or rectangle (r): "

    heading = "Shape {} of {}".format(shapes, shape_amount)

    print(heading)
    choose_error = "Please choose a shape from the options above"
    user_choice = choice_checker(choose_instruction, shape_list, choose_error)
    print()

    print("You chose: {}".format(user_choice))
