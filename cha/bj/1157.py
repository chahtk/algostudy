string = input()

bit = [0]*100

for s in string:
  bit[ord(s.upper())] += 1

count = 0
maxNum = max(bit)
maxChar = ''
for i in range(65, 91):
  if maxNum == bit[i]:
    maxChar = chr(i)
    count += 1
print(maxChar.upper() if count == 1 else '?')