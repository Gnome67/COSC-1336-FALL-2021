"""
Talha Sohail
2092858
COSC 1336
Assignment 12
"""

def findFrequencies(bigram):
  pairs = []
  for index in range(len(bigram)-1):
    pairs.append(bigram[index:index+2])
  return pairs

bigram = []
with open("zingarelli2005.txt") as file:
  for line in file.readlines():
    word = line.strip()
    bigram.append(word)
if(FileNotFoundError == True):
  print("Error finding file.")
  SystemExit

result = {}
print("The bigram frequencies are...")
for word in bigram:
  answer = findFrequencies(word)
  for pair in answer:
    if pair in result:
      result[pair] += 1
    else:
      result[pair] = 1

text = "{} = {:0.4f}%"
for key in sorted(result):
  print(text.format(key,result[key]/sum(result.values())*100))
