x = int(input())

binary = bin(x)
count = 0

for i in range(2,len(binary)):
  if binary[i] == '1':
    count+=1

print(count)