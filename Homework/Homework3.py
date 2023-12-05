"""
Talha Sohail
2092858
COSC 1336
Homework 3
"""

words = {}
anagrams = {}
max_group = 0

with open("words.txt") as file:
  for line in file.readlines():
    word = line.strip()
    length = len(word)
    if length in words:
      words[length].append(word)
    else:
      words[length] = [word]   
    letters = list(word)
    letters.sort()
    signature = tuple(letters)
    if signature in anagrams:
      anagrams[signature].append(word)
      if max_group < len(anagrams[signature]):
        max_group = len(anagrams[signature])
    else:
      anagrams[signature] = [word]
if(FileNotFoundError == True):
  print("Error finding file.")

def findAnagram(word):
  letters = list(word)
  letters.sort()
  letters = tuple(letters)
  print("\nThe anagrams for {} are:".format(word))
  print(anagrams[letters])

def findwordLength(number):
  wordLength = words[number]
  while True:
    if not wordLength:
      break
    word = wordLength[0]
    letters = list(word)
    letters.sort()
    letters = tuple(letters)
    print(anagrams[letters])
    for word in anagrams[letters]:
      wordLength.remove(word)

def findgroupLength(group):
  y = [x for l in list(words.values()) for x in l]
  while True:
    if not y:
      break
    word = y[0]
    letters = list(word)
    letters.sort()
    letters = tuple(letters)
    if len(anagrams[letters]) == group: 
      print(anagrams[letters])
    for word in anagrams[letters]:
      y.remove(word)


def print_menu():
    print()
    print("*"*40)
    print("1. Find the anagrams of a word")
    print("2. Display the anagram groups by word length")
    print("3. Display the anagram groups by group length")
    print("0. Exit")
    print("*"*40)
    

def ask_selection():
    selection = int(input("Please enter your selection: "))
    while selection < 0 or selection > 3:
        print("Invalid selection >>"+str(selection)+"<<.")
        selection = int(input("Please enter your selection: "))
        
    return selection


while True:
    print_menu()
    selection = ask_selection()
    if(selection == 1):
      word = input("Please enter the word you wish to find: ").upper()
      while word not in words[len(word)]:
        print("Sorry, >>",word,"<< was not found.")
        word = input("Please enter the word you wish to find: ").upper()
      findAnagram(word)
    elif(selection == 2):
      lengths = list(words.keys())
      min_len = lengths[0]
      max_len = lengths[len(lengths)-1]
      number = int(input("Please enter the length of the words to display({}-{}): ".format(min_len,max_len)))
      while number < min_len or number > max_len:
        number = int(input("Invalid number, please enter a valid number: "))
      findwordLength(number)
    elif(selection == 3):
      min_group = 1
      group = int(input("Please enter the anagram group size ({}-{}): ".format(min_group,max_group)))
      while(group > max_group or group < min_group):
        group = int(input("Invalid number, please enter a valid number: "))
      findgroupLength(group)
    if(selection == 0):
        break
    
print("Goodbye!")