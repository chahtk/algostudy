from collections import deque

t = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]
resArr = []

for _ in range(t):
  [m, n, k] = list(map(int, input().split()))
  arr = [[0]*m for _ in range(n)]
  
  for _ in range(k):
    [x, y] = list(map(int, input().split()))
    arr[y][x] = 1
  
  que = deque()
  res = 0
  for i, row in enumerate(arr):
    for j, col in enumerate(row):
      if col == 1:
        que.append([i, j])
        arr[i][j] = 0
        while len(que) > 0:
          [qx, qy] = que.popleft()
          for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
              continue
            if arr[nx][ny] == 1:
              que.append([nx, ny])
              arr[nx][ny] = 0
        res += 1
  resArr.append(res)

for res in resArr:
  print(res)
