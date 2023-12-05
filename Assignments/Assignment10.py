"""
Talha Sohail
2092858
COSC 1336
Assignment 10
"""

"""def NumToStr(numOne,numTwo):
  strOne = ""
  strTwo = ""
  for x in range(0,len(numOne),1):
    if(numOne[x] == "1"):
      strOne += "L" or "I"
    elif(numOne[x] == "2"):
      strOne += "A" or "B" or "C"
    elif(numOne[x] == "3"):
      strOne += "D" or "E" or "F"
    elif(numOne[x] == "4"):
      strOne += "G" or "H"
    elif(numOne[x] == "5"):
      strOne += "J" or "K"
    elif(numOne[x] == "6"):
      strOne += "M" or "N"
    elif(numOne[x] == "7"):
      strOne += "P" or "Q" or "R" or "S"
    elif(numOne[x] == "8"):
      strOne += "T" or "U" or "V"
    elif(numOne[x] == "9"):
      strOne += "W" or "X" or "Y" or "Z"
    elif(numOne[x] == "O"):
      strOne += "0"
  for x in range(0,len(numTwo),1):
    if(numTwo[x] == "1"):
      strTwo += "L" or "I" 
    elif(numTwo[x] == "2"):
      strTwo += "A" or "B" or "C"
    elif(numTwo[x] == "3"):
      strTwo += "D" or "E" or "F"
    elif(numTwo[x] == "4"):
      strTwo += "G" or "H"
    elif(numTwo[x] == "5"):
      strTwo += "J" or "K"
    elif(numTwo[x] == "6"):
      strTwo += "M" or "N"
    elif(numTwo[x] == "7"):
      strTwo += "P" or "Q" or "R" or "S"
    elif(numTwo[x] == "8"):
      strTwo += "T" or "U" or "V"
    elif(numTwo[x] == "9"):
      strTwo += "W" or "X" or "Y" or "Z"
    elif(numTwo[x] == "0"):
      strTwo += "0"
  strThree = strOne + strTwo
  return strThree
print(NumToStr(numberOne,numberTwo))"""

def get_letters(digit):
    key_pad = {"0":["O"], "1":["I", "L"],"2":["A","B","C"], "3":["D","E","F"], "4":["G","H"], "5":["J","K"], "6":["M","N"], "7":["P","Q","R","S"], "8":["T","U","V"], "9":["W","X","Y","Z"]}
    return key_pad[digit]


def magic(first, second):
    result = []
    for a in first:
      for b in second:
        result.append(a+b)
    return result


def get_combos(digits):
    
    result = [""]
    
    for index in range(len(digits)):
        letters = get_letters(digits[index])
        result = magic(result, letters)
    
    return result

three_letter_words = []
four_letter_words = []

try:
    with open("words.txt") as words_file:
        for word in words_file.readlines():
            word = word.strip()
            if len(word) == 3:
                three_letter_words.append(word)
            elif len(word) == 4:
                four_letter_words.append(word)

except FileNotFoundError:
    print("oops the file is missing!")

def askAgain():
  inputMe = input("Would you like to input a number? (Y/N): ")
  while(inputMe.upper() == "Y"):
    number = input("Please enter a phone number: ")
    first_part = number[:3]
    second_part = number[4:]
    possible_words = get_combos(first_part)
    good_words = []
    for possible in possible_words:
      if possible in three_letter_words:
          good_words.append(possible)
    possibleWordsTwo = get_combos(second_part)
    good_wordsTwo = []
    for possible in possibleWordsTwo:
      if possible in four_letter_words:
        good_wordsTwo.append(possible)
    good_wordsThree = magic(good_words,["-"])
    good_wordsThree = magic(good_wordsThree,good_wordsTwo)
    for x in range(0,len(good_wordsThree),1):
      print(good_wordsThree[x])
    inputMe = input("Would you like to input a number? (Y/N): ")
  else:
    print("Goodbye!")

askAgain()