from sys import stdin
lines = []

while True:
  line = stdin.readline().rstrip('\n')
  if not line:
    break
  lines.append(line)

for line in lines:
  a,b,c,d = 0,0,0,0
  for l in line:
    if l.islower():
      a+=1
    if l.isupper():
      b+=1
    if l.isdigit():
      c+=1
    if l.isspace():
      d+=1
  print(a,b,c,d)