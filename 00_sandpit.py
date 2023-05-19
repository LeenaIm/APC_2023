try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
except ValueError:
    print("Invalid input! Please enter a numeric value for length and width.")
else:
    area = length * width
    perimeter = 2 * (length + width)

    print()
    print("The area of the rectangle is:", area)
    print("The perimeter of the rectangle is:", perimeter)
