"""
Talha Sohail
2092858
COSC 1336
Assignment 11
"""
import time

def checkTriangle(a,b,c):
  return a**2 + b**2 == c**2

start = time.time()
value = 2021
dictionary = {}

for a in range(1,value):
  for b in range(a+1,value):
    for c in range(b+1,value):
      if checkTriangle(a,b,c):
        perimeter = a+b+c
        if(perimeter in dictionary):
          dictionary[perimeter].append((a,b,c))
        else:
          dictionary[perimeter] = [ (a,b,c) ]

bestPerimeter = 0
mostTriangles = 0
for perimeter in sorted(dictionary):
  length = len(dictionary[perimeter])
  if(length > mostTriangles):
    bestPerimeter = perimeter
    mostTriangles = length
    dictionaryList = dictionary[perimeter]

print("The perimeter of {} gives a maximum value of {} triangle(s).".format(bestPerimeter,mostTriangles))
print("The triangles are: ")
for abc in sorted(dictionaryList):
  print(abc)
print(time.time() - start)