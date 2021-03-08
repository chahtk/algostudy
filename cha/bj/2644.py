from collections import deque

# input
n = int(input())
[target1, target2] = list(map(int, input().split()))
m = int(input())

# init arr
arr = [[0] for _ in range(n+1)]
visit = [False] * (n+1)
parent = set()
child = set()

for _ in range(m):
  [x, y] = list(map(int, input().split()))
  parent.add(x)
  child.add(y)
  if arr[x] == [0]:
    arr[x] = [y]
  else:
    arr[x].append(y)

# find root
root = list(parent-child)
r1, r2 = 0, 0
flagR1, flagR2 = 0, 0

for r in root:
  que = deque()
  que.append([arr[r], 1])
  visit[r] = True
  
  while len(que) > 0:
    [nowArr, count] = que.pop()
    for narr in nowArr:
      if narr == target1:
        r1 = count
        flagR1 = r
      if narr == target2:
        r2 = count
        flagR2 = r
      if not visit[narr]:
        visit[narr] = True
        if arr[narr][0] == 0: 
          continue
        que.append([arr[narr], count+1])

if flagR1 != flagR2:
  print(-1)
else:
  print(r1+r2)
