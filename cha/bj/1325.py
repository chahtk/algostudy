n, m = list(map(int, input().split()))
arr = [ [] for _ in range(n+1)]

for _ in range(m):
  a,b = list(map(int, input().split()))
  arr[b].append(a)

stk = []
ans = {}
maxCount = 0
for i in range(1, n+1):
  visit = [False] * (n+1)
  stk.append(i)
  count = 1
  while len(stk) > 0:
    el = stk.pop()
    for nextEl in arr[el]:
      if not visit[nextEl]:
        stk.append(nextEl)
        visit[nextEl] = True
        count += 1
  if maxCount <= count:
    maxCount = count
    if not count in ans:
      ans[count] = [i]
    else:
      ans[count].append(i)

maxKey = max(ans.keys())
sortedAns = sorted(ans[maxKey])

for el in sortedAns:
  print(el, end=' ')
