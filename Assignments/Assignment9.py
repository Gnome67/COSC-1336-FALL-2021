"""
Talha Sohail
2092858
COSC 1336
Assignment 9
"""

def linearSearch(passwords,choice):
  counter = 1
  for x in range(len(passwords)): 
    if(passwords[x]==choice):
      return (True,counter)
    else:
      counter += 1
  return (False,counter)

def binarySearch(passwords,choice):
  low = 0
  high = len(passwords) - 1
  counter = 0
  while(low <= high):
    counter += 1
    mid = (high + low)//2
    if(choice == passwords[mid]):
      return (True,counter)
    elif(choice > passwords[mid]):
      low = mid + 1
    elif(choice < passwords[mid]):
      high = mid - 1
  return (False, counter)

with open("passwords_short.txt") as file:
  lines = file.readlines()
passwords = []
for line in lines:
  passwords.append(line.strip())

choice = input("Please input a word to check the list with: ")
answer, counter = binarySearch(passwords,choice)
answerTwo, counterTwo = linearSearch(passwords,choice)
if answer == True:
  print("Found after", counter, "tries (Binary Search). Please change it immediately!")
else:
  print("Password not found after", counter,"tries. You are safe... for now...")
if answerTwo == True:
  print("Found after", counterTwo, "tries (Linear Search). Please change it immediately!")
else:
  print("Password not found after", counterTwo,"tries. You are safe... for now...")