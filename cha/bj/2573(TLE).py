import copy
from collections import deque

[n, m] = list(map(int, input().split()))

arr = [[]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]

def initVisit(arr, visit):
  notZero = []
  for i in range(n):
    for j in range(m):
      if arr[i][j] != 0:
        visit[i][j] = False
        notZero.append([i,j])
      else:
        visit[i][j] = True
  return notZero

for i in range(n):
  line = list(map(int, input().split()))
  arr[i] = line

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

years = 0
while True:
  years += 1
  part = 0
  notZero = initVisit(arr, visit)
  tempArr = copy.deepcopy(arr)
  for i, j in notZero:
    if visit[i][j]:
      continue
    visit[i][j] = True
    part += 1
    que = deque([[i,j]])
    while len(que) > 0:
      x, y = que.popleft()
      for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
          if tempArr[nx][ny] == 0:
            arr[x][y] = max(0, arr[x][y]-1)
          else:
            if visit[nx][ny]:
              continue
            que.append([nx, ny])
            visit[nx][ny] = True

  if part == 0:
    years = 1
  if part >= 2:
    break

print(years-1)