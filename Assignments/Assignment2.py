"""
Talha Sohail
2092858
COSC 1336
Assignment #2: Turtles
"""

import turtle

#defining variables
subDivisions = int(input("Please enter the number of subdivisions: "))
borderDefine = (subDivisions * 10)
borderWidth = 1
verticalLength = 0
horizontalLength = 0


#starting turtle graphics
scn = turtle.Screen()
turtle.mode('logo')
turtle.speed(10)
turtle.shape('turtle')
turtle.width(borderWidth)

#Drawing border
for i in range(4):
  turtle.forward(borderDefine)
  turtle.right(90)

#Drawing vertical lines
turtle.goto(verticalLength,0)
turtle.forward(borderDefine)
for i in range(subDivisions):
  turtle.penup()
  turtle.goto(verticalLength,0)
  turtle.pendown()
  turtle.forward(borderDefine)
  verticalLength = verticalLength + 10


#Drawing horizontal lines
turtle.penup()
turtle.goto(0,horizontalLength)
turtle.pendown()
turtle.right(90)
turtle.forward(borderDefine)
for i in range(subDivisions):
  turtle.penup()
  turtle.goto(0,horizontalLength)
  turtle.pendown()
  turtle.forward(borderDefine)
  horizontalLength = horizontalLength + 10
"""
#Bonus
subDivisionsBonus = int(input("Please enter the number of subdivisions for the bonus: "))
turtle.clear()
borderDefineBonus = (subDivisionsBonus * 10)
borderWidth = 3
crossWidth = 1
crossGap = (subDivisionsBonus / 2)

#Bonus drawing border
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.width(borderWidth)
for i in range(4):
  turtle.forward(borderDefineBonus)
  turtle.left(90)
turtle.width(crossWidth)

# Bonus Dots
length = 10
length2 = 10
for i in range(subDivisionsBonus):
  turtle.penup()
  turtle.goto(length, length2)
  turtle.dot()
  turtle.pendown()
  length = length + 10

#Bonus Crosses
scn.exitonclick()
"""