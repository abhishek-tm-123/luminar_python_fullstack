"""
read box1_width,box1_height,box2_width,box2_height

evealuate box1_width and height larger than box2

"""

b1_width = int(input("enter b1 width "))

b1_height = int(input("enter b1 height "))

b2_width = int(input("enter b2 width "))

b2_height = int(input("enter b2 height "))

is_b1_large = b1_width > b2_width and b1_height > b2_height

print(is_b1_large)