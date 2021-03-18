t = int(input())
res = []
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  arr.sort()

  ans = 'YES'
  for i in range(n-1):
    diff = arr[i+1] - arr[i]
    if diff > 1:
      ans = 'NO'
  res.append(ans)

for r in res:
  print(r)