s = "thisisastringwithabcsinit"
newString = ""
inChars = map(lambda c: c, s)

for c in s:
  if c >= s[s.find(c) + 1]:
    newString += c + s[s.find(c) + 1]

