from collections import deque

n = int(input())

arr = [[0] * n for _ in range(n)]
height = set()
que = deque()
resMax = 1

# define dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
  arr[i] = list(map(int, input().split()))
  for j in arr[i]:
    height.add(j)

for h in list(height):
  # 침수 지역
  visit = [[False]*n for _ in range(n)]
  # 침수 지역 체크
  for i in range(n):
    for j in range(n):
      if arr[i][j] <= h:
        visit[i][j] = True
  # que
  res = 0
  for i in range(n):
    for j in range(n):
      if not visit[i][j]:
        que.append([i, j])
        visit[i][j] = True
        while len(que) > 0:
          [x, y] = que.popleft()
          for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or ny<0 or nx>=n or ny>=n:
              continue
            if not visit[nx][ny]:
              visit[nx][ny] = True
              que.append([nx, ny])
        res += 1
  resMax = res if res > resMax else resMax

print(resMax)