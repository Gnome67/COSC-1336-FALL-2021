"""
Talha Sohail
2092858
COSC 1336
Assignment #1
"""
import math

circ_r = float(input("Please enter the radius of a circle: "))

#calculate area of circle
area_circle = (circ_r ** 2) * math.pi
#calculate area of hexagon
area_hexagon = (3 * math.sqrt(3))/2 * (circ_r ** 2)
#calculate difference between circle and hexagon
shaded_area = area_circle - area_hexagon
print("="*50)
print("Area of circle is  = ", "{:.6f}".format(area_circle))
print("Area of hexagon is = ", "{:.6f}".format(area_hexagon))
print("Area of difference = ", "{:.6f}".format(shaded_area))
print("="*50)

#Bonus section
#find the radius where the the shaded_area is equal to the radius up to 6 numbers

circ_r2 = float(circ_r)
while shaded_area != circ_r2:
  circ_r2 = circ_r + 0.000001
else:
  print("The radius equal to the shaded area is: ", circ_r2)

#conclusion: Not sure how to do this without lowering the amount of decimals outputted by shaded_area because the 7th decimal will never match up.