"""
Talha Sohail
2092858
COSC 1336
Assignment 6
"""
def Menu():
  print("Please choose from the following shapes. Please note for the diamond options your number must be odd. \n1. Square\n2. Rectangle\n3. Right Triangle (Right)\n4. Right Triangle (Left)\n5. Diamond\n0. Exit ")

def drawSquare(a):
  for x in range(a):
    print("X"*a)

def drawRect(b,f):
  for x in range(b):
    print("X"*f)

def drawRTri(c):
  for x in range(c+1):
    print("^"*x)

def drawLTri(d):
  for x in range(d+1):
    print(" "*(d-x)+"^"*x)

def drawDiamond(e):
  for a1 in range(1, (e+1)//2 + 1): #top
    for a2 in range((e+1)//2 - a1):
      print(" ", end = "")
    for a3 in range((a1*2)-1):
      print("^", end = "")
    print()
  for a1 in range((e+1)//2 + 1, e + 1): #bottom
    for a2 in range(a1 - (e+1)//2):
      print(" ", end = "")
    for a3 in range((e+1 - a1)*2 - 1):
      print("v", end = "")
    print()
  

shapeChoose = 0
Menu()
shapeChoose = int(input(""))
while(shapeChoose < 0 or shapeChoose > 5):
  print("Invalid. You input: ",shapeChoose)
  shapeChoose = int(input("Choose a number shown. "))
  Menu()
if(shapeChoose == 0):
    print("Goodbye")
print("You have chosen option", shapeChoose)
shapeInput = int(input("Please enter the size of the shape: "))
while(shapeInput < 0):
  shapeInput = int(input("Please enter a number higher than 0: "))

if(shapeChoose == 1):
  drawSquare(shapeInput)
elif(shapeChoose == 2):
  rectTwo = int(input("Please input a second variable for the rectangle: "))
  drawRect(shapeInput,rectTwo)
elif(shapeChoose == 3):
  drawRTri(shapeInput)
elif(shapeChoose == 4):
  drawLTri(shapeInput)
elif(shapeChoose == 5):
  while(shapeInput % 2 == 0):
    print("You entered ",shapeInput," which is an even number.")
    shapeInput = int(input("Please input an odd number: "))
  drawDiamond(shapeInput)
else:
  print("Error.")