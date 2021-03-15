m = int(input())
arr = []

for _ in range(m):
  arr.append(list(map(int, input().split())))

ansDir = 0 # clock. 1:cc
ansRot = 1

for item in arr:
  ratio = item[1]/item[0]
  direction = item[2]

  ansRot *= ratio
  if direction == 1:
    ansDir = 0 if ansDir == 1 else 1

print(ansDir, round(ansRot))