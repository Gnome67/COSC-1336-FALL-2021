"""
Talha Sohail
2092858
COSC 1336
Homework 2
"""

#Bonus here if i felt like it

def findGain(data):
  bDate = data[0][0]
  bPrice = data[0][0]
  maxProfit = 0.0
  ratio = 0.0
  for index in range(1,len(data)):
    sDate = data[index][0]
    sPrice = data[index][1]
    for index in range(1,len(data)):
      bDate = data[index][0]
      bPrice = data[index][2]
      profit = sPrice - bPrice
      if profit >+ maxProfit:
        maxProfit = profit
        maxSDate = sDate
        maxBDate = bDate
        maxBPrice = bPrice
        maxSPrice = sPrice
        ratio = maxSPrice/maxBPrice
  print("*"*40)
  print("The maximum profit is {:0.2f} per share".format(maxProfit))
  print()
  print("Buy on {} at a price of {:0.2f}".format(maxBDate,maxBPrice))
  print("Sell on {} at a price of {:0.2f}".format(maxSDate,maxSPrice))
  print("Change in value ratio: {:0.2f}".format(ratio))
  print()
  print("*"*40)

def findCSV():
  while True:
    try:
      csv = input("Please enter the data file name: ")
      if(csv == ""):
        return 0
      else:
        open(csv)
        print("Reading data...")
        return csv
    except (FileNotFoundError):
        csv = input("Error reading data. Please check the name and try again: ")

csv = findCSV()
if(csv == 0):
  print("Goodbye!")
data = []
with open(csv) as file:
  lines = file.readlines()
for index in range(1,len(lines)):
  line = lines[index]
  parts = line.split(',')
  data.append((parts[0],float(parts[2]),float(parts[3])))
findGain(data)