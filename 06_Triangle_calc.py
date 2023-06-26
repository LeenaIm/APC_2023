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
print()
choose_error = "Please choose a shape from the options above"
user_choice = choice_checker(choose_instruction, shape_list, choose_error)

# if user chooses triangle, asks for base and height to calculate the area and perimeter
# print error message if user does not enter number for base and height
if user_choice == "triangle":
    valid_input = False
    while not valid_input:
        try:
            base = float(input("Enter the base of the triangle: ".format(user_choice)))
            height = float(input("Enter the height of the triangle: ".format(user_choice)))
            print()
            sideA = float(input("Enter side A of the triangle: ".format(user_choice)))
            sideB = float(input("Enter side B of the triangle: ".format(user_choice)))
            sideC = float(input("Enter the side C of the triangle: ".format(user_choice)))
            valid_input = True
        except ValueError:
            print("Error! Please enter a number for the base and height.")
            print()

    area = 0.5 * base * height
    perimeter = sideA + sideB + sideC

    print()
    print("The area of the triangle is: {}".format(area))
    print("The perimeter of the triangle is: {}".format(perimeter))
    print()
