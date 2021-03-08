[c, p] = list(map(int, input().split()))
p -= 1
feild = list(map(int, input().split()))

blocks = [
  [[0], [0,0,0,0]],
  [[0,0]],
  [[0,0,1], [1,0]],
  [[1,1,0], [0,1]],
  [[0,0,0], [1,0,1], [1,0], [0,1]],
  [[0,0,0], [0,1,1], [2,0], [0,0]],
  [[0,0,0], [0,0], [0,2], [1,1,0]],
]

res = 0

for i in range(len(feild)):
  for block in blocks[p]:
    prev = feild[i] - block[0]
    if prev < 0:
      continue
    flag = True
    for j in range(1,len(block)):
      if i + j >= c:
        flag = False
        break
      print(prev, i, j, feild[i+j], block[j])
      if prev != feild[i+j] - block[j]:
        falg = False
        break
    if falg:
      res += 1

print(res)