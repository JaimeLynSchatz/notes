import re
import sys

s = sys.argv[1]
vowels = "aeiou"

vowelCount = 0
for c in s:
  if vowels.find(c) >= 0: 
    vowelCount += 1
print "Number of vowels: " + str(vowelCount)  

