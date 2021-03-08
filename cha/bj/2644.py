from collections import deque

n = int(input())
[tg1, tg2] = list(map(int, input().split()))
m = int(input())

arr = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
  [x,y] = list(map(int, input().split()))
  arr[x].append(y)
  arr[y].append(x)

que = deque()
que.append([tg1, 0])
visit[tg1] = True
ans = -1

while len(que) > 0:
  [x, count]  = que.pop()
  if x == tg2:
    ans = count
    break
  for nextX in arr[x]:
    if not visit[nextX]:
      que.append([nextX, count + 1])
      visit[nextX] = True

print(ans)