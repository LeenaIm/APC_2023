import pandas

column = ["Chicken", "Cow", "Sheep"]
titled_column = {"name": column,
                 "height": [1.45, 1.98, 1.24],
                 "weight": [40, 20, 10]}
data = pandas.DataFrame(titled_column)
print(data)

all_shapes = []
all_dimensions = []
all_perimeters = []
all_areas = []

shape_dict = {
    "Shape": all_shapes,
    "Dimensions": all_dimensions,
    "Perimeter": all_perimeters,
    "Area": all_areas
}