"""
Talha Sohail
2092858
COSC 1336
Assignment 3
"""

import math
#The user inputs a number
floatInput = float(input("Please enter a number: "))
if(floatInput <= 0):
  #Makes sure the number isnt negative
  floatInput = float(input("Invalid. Please enter a positive number: "))
print("="*40)
#The output used to show the various roots
output = float(floatInput)
#defining loop
x = 1
output = (output + floatInput/output) / 2
output = (output + floatInput/output) / 2
print(x," = ",output)
#Calculating the roots using a loop
x = 2
while(x != 33):
  #Newtonian Method
  output = (output + floatInput/output) / 2
  if(x == 2 or x == 4 or x == 8 or x == 16 or x == 32):
    print(x," = ", output)
  x = x+1
#Shows the correct square root
rootCorrect = math.sqrt(floatInput)
print("sqrt = ", rootCorrect)
print("="*40)
print("Thank you, goodbye!")