"""
Talha Sohail
2092858
COSC 1336
Assignment 5
"""
def give_Grade(x):
  if(x >= 90):
    return "A"
  elif(86 <= x < 90):
    return "A-"
  elif(82 <= x < 86):
    return "B+"
  elif(78 <= x < 82):
    return "B"
  elif(74 <= x < 78):
    return "B-"
  elif(70 <= x <= 74):
    return "C+"
  elif(66 <= x <= 70):
    return "C"
  elif(62 <= x < 66):
    return "C-"
  elif(58 <= x < 62):
    return "D+"
  elif(54 <= x < 58):
    return "D"
  elif(51 <= x < 55):
    return "D-"
  else:
    return "F"
#bonus
def give_Estimate(y):
  if(y >= 90):
    return "0"
  elif(86 <= y < 90):
    return 90 - y
  elif(82 <= y < 86):
    return 86 - y
  elif(78 <= y < 82):
    return 82 - y
  elif(74 <= y < 78):
    return 78 - y
  elif(70 <= y <= 74):
    return 74 - y
  elif(66 <= y <= 70):
    return 70 - y
  elif(62 <= y < 66):
    return 66 - y
  elif(58 <= y < 62):
    return 62 - y
  elif(54 <= y < 58):
    return 58 - y
  elif(51 <= y < 55):
    return 55 - y
  else:
    return 50 - y
#Ask for input
avgFinal = float(input("Please input a final average: "))
gradeLetter = give_Grade(avgFinal)
print()
print()
print("Congratulations, your grade is a "+gradeLetter)
estimateLeft = give_Estimate(avgFinal)
print("You are ",estimateLeft," points away from the next letter grade.")