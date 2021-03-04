from collections import deque
from sys import stdin
deq = deque([])
res = []

def solve(line):
  mode = line[0]

  if mode == 'push':
    deq.append(int(line[1]))
  elif mode == 'pop':
    res.append(deq.popleft() if len(deq)>0 else -1)
  elif mode == 'size':
    res.append(len(deq))
  elif mode == 'empty':
    res.append(1 if len(deq)==0 else 0) # 삼항연산자
  elif mode == 'front':
    res.append(deq[0] if len(deq)>0 else -1)
  elif mode == 'back':
    res.append(deq[len(deq)-1] if len(deq)>0 else -1)

n = int(input())
for _ in range(n):
  line = stdin.readline().split()
  solve(line)

for item in res:
  print(item)