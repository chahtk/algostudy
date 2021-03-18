t = int(input())
res = []
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  allComb = set()
  for i in range(n):
    for j in range(i+1, n):
      allComb.add(arr[i]+arr[j])
  
  allComb = list(allComb)
  allComb.sort()
  maxCount = 0
  for ac in allComb:
    visit = [False] * n
    count = 0
    
    for i in range(n):
      for j in range(i+1, n):
        if arr[i] + arr[j] == ac:
          if visit[i] == False and visit[j] == False:
            visit[i] = True
            visit[j] = True
            count += 1
    maxCount = max(count, maxCount)
  res.append(maxCount)

for r in res:
  print(r)