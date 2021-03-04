res = 0

n = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))

prev = 2e9

for idx, val in enumerate(oil):
  if len(dist) > idx:
    if prev > val:
      prev = val
    res += prev * dist[idx]

print(res)