t = int(input())
res = []

for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  count = 0
  prev = arr[0]

  for i in range(1,n):
    if max(prev, arr[i]) <= 2 * min(prev,arr[i]):
      prev = arr[i]
    else:
      while max(prev, arr[i]) > 2 * min(prev,arr[i]):
        count += 1
        if prev > arr[i]:
          if prev % 2 == 0:
            prev = prev // 2
          else:
            prev = prev // 2 + 1
        else:
          prev = prev * 2
      prev = arr[i]
  res.append(count)

for r in res:
  print(r)