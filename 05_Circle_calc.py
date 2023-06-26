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


shape_list = ["triangle", "square", "circle", "rectangle"]
choose_instruction = "Please choose from square (s), rectangle (r), triangle (t) or circle (c): "
choose_error = "Please choose a shape from the options above"
user_choice = choice_checker(choose_instruction, shape_list, choose_error)

# if user chooses circle, ask for radius and circumference to calculate the area and perimeter
# calculates area and perimeter
# prints error message if user does not enter number for radius
if user_choice == "circle":
    valid_input = False
    while not valid_input:
        try:
            radius = float(input("Enter the radius of the circle: ".format(user_choice)))
            valid_input = True
        except ValueError:
            print("Error! Please enter a number for the radius.")
            print()

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print()
    print("The area of the circle is: {}".format(area))
    print("The perimeter of the circle is: {}".format(circumference))
    print()
