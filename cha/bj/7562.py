from collections import deque

t = int(input())

dir = [[-2, -1], [-1, -2], [1,-2], [2,-1], [-1,2], [-2,1] ,[1,2], [2,1]]

for _ in range(t):
  l = int(input())
  visit = [[False]*l for _ in range(l)]
  nextMove = []
  knight = list(map(int, input().split()))
  dist = list(map(int, input().split()))

  que = deque([[knight[0], knight[1],0]])
  visit[knight[0]][knight[1]] = True
  while len(que) > 0:
    pos = que.popleft()
    cnt = pos[2]
    if pos[0] == dist[0] and pos[1] == dist[1]:
      print(cnt)
      break
    for d in dir:
      x = pos[0] + d[0]
      y = pos[1] + d[1]
      if x < 0 or y < 0 or x >= l or y >= l:
        continue
      if not visit[x][y]:
        visit[x][y] = True
        que.append([x, y, cnt+1])
