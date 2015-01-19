import re

s = "thissbobobtringhasbobinit"

# of use:
# s = "yourstring"
# s = map(lambda c: c, s)
# s now is ['y', 'o', 'u', etc]
#
# to bring them back
# ''.join(s)

bob = "bob"
bobCount = 0

foundAt = s.find(bob)
print "This is Echo 4 to Echo Base: " + str(foundAt)

while foundAt >= 0:
  bobCount += 1
  s = s[foundAt + 1:]
  foundAt = s.find(bob)
  if foundAt == -1:
    print "D'oh! No more Bobs"
    break

print "Number of times bob occurs is: " + str(bobCount)
