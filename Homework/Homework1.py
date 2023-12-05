"""
Talha Sohail
2092858
COSC 1336
Homework 1
"""

topCoord = float(input("Please enter a x coordinate: "))
bottomCoord = float(input("Please enter a y coordinate:" ))
leftSideCoord = float(input("Please enter a width: "))
rightSideCoord = float(input("Please enter a height: "))
width = 121
height = 61

def in_mandelbrocht(c):
  z= 0
  for a in range(1000):
    z = z**2 + c
    temp = abs(z)
    if temp > 2:
      return False
  return True

width = 121
height = 61

def find_x(x):
  x = topCoord - leftSideCoord/2 + leftSideCoord * column / (width-1)
  return x

def find_y(y):
  y = bottomCoord - rightSideCoord/2 + rightSideCoord * row / (height - 1)
  return y

for row in range(height):
  for column in range(width):
    b = find_x(column)
    c = find_y(row)
    d = complex(b,c)

    if(b == 0 and c == 0):
      print("+", end="")
    elif(b == 0):
      print("|", end="")
    elif(c == 0):
      print("-", end="")
    elif in_mandelbrocht(d):
      print("*", end="")
    else:
      print(" ", end="")
  print()