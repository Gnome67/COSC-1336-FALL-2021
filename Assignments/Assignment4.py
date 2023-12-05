"""
Talha Sohail
2092858
COSC 1336
Assignment 4
"""

import time
import math
print("Estimating Pi!")
print()
start = time.time()
#function
def estimate_pi(userexp):
  result = 0.0
  for n in range(10**userexp):
      result += (-1.0)**n/(2.0*n+1.0)
  return 4*result
#only 1 input
powers = int(input("Please enter the maximum powers of ten: "))
print("="*40)
for x in range(powers+1):
  start = time.time()
  print("10^",str(x)," -> ",estimate_pi(x), " \t ", (time.time()-start))
start = time.time()
print(math.pi, " \t ", (time.time()-start))
print("="*40)
print("Thank you, goodbye!")