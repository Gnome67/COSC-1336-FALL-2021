"""
Talha Sohail
2092858
COSC 1336
Homework #0
"""
import math

length = int(input("Input the length of the room: "))
width = int(input("Input the width of the room: "))
height = int(input("Input the height of the room: "))
paint_gallon = 400
area = length * height
area_2 = width * height
area_ceil = length * width
area_total = (area * 2) + (area_2 * 2) + (area_ceil)
area_gallon = math.ceil(area_total / paint_gallon)
area_floor = area_ceil * 9

print("You would need ", area_gallon, " gallons in order to cover the walls and ceiling.")
print("You would need ", area_floor, " tiles to cover the floor with.")