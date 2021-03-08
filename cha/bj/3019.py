[c, p] = list(map(int, input().split()))
p -= 1
feild = list(map(int, input().split()))

blocks = [
  [[0], [0,0,0,0]],
  [[0,0]],
  [[0,0,1], [1,0]],
  [[1,0,0], [0,1]],
  [[0,0,0], [1,0,1], [1,0], [0,1]],
  [[0,0,0], [0,1,1], [2,0], [0,0]],
  [[0,0,0], [0,0], [0,2], [1,1,0]],
]

res = 0

for i in range(len(feild)):
  for block in blocks[p]:
    firstValue = feild[i] - block[0]
    if firstValue < 0:
      continue
    flag = True
    for j in range(1,len(block)):
      if i + j >= c or firstValue != feild[i+j] - block[j]:
        flag = False
        break
    if flag:
      res += 1

print(res)