"""
Talha Sohail
2092858
COSC 1336
Assignment 7
"""

def latinVowel(word):
  capitalizeEnd = 0
  if(word[0].istitle() == True):
    capitalizeEnd = True
  wordList = word.lower().split()
  word = []
  for word in wordList:
      if word[0] in 'aeiouAIEOU': #case where vowel is first
          word.append('way')
      else:
        for letter in word:
          if letter in 'aeiouAIEOU':
            word = word[word.index(letter):] + word[:word.index(letter)] +'ay'
            break
  word = "".join(word)
  if(capitalizeEnd == True):
    return word.capitalize()
  elif(capitalizeEnd == False):
    return word

def askAgain(latinChoice):
  while(latinChoice.upper() == "Y"):
    latinVar = input("Please input a word you would like to convert: ")
    print(latinVar+" becomes "+latinVowel(latinVar))
    latinChoice = input("Do you want to input another word? Y/N: ")
  if(latinChoice.upper() == "N"):
    print("Ankthay ouyay!")

latinVar = input("Please input a word you would like to convert to Pig Latin: ")
print(latinVar+" becomes "+latinVowel(latinVar))
latinChoice = input("Do you want to input another word? Y/N: ")
askAgain(latinChoice)