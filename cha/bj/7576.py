from collections import deque

que = deque()

# input m, n
[m, n] = list(map(int, input().split()))
# init box, visit
box = [[0]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]
# define check fresh tomato
fresh = False
freshCount = 0

# input data
for i in range(n):
  line = list(map(int, input().split()))
  box[i] = line
  for idx, j in enumerate(line):
    if j == 0:
      fresh = True
      freshCount += 1
    if j == 1:
      que.append([i, idx, 0])
      visit[i][idx] = True
    if j == -1:
      visit[i][idx] = True

if not fresh:
  print(0)
  exit()

# define dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# define result
result = 0

while len(que) > 0:
  [x, y, cnt] = que.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<0 or ny<0 or nx>=n or ny>=m:
      continue
    if not visit[nx][ny]:
      visit[nx][ny] = True
      que.append([nx, ny, cnt+1])
      freshCount -= 1
      result = cnt+1 if result < cnt+1 else result

if freshCount == 0:
  print(result)
else:
  print(-1)