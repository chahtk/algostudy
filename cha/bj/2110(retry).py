import sys

[n, c] = list(map(int, sys.stdin.readline().split()))
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

# find dist
start, end = 1, arr[-1] - arr[0]
ansMax = 0

if end == 1:
  print(1)
  exit()

while start<end:
  mid = (start+end)//2
  count = 1
  left = arr[0]
  for i in range(1, n):
    if mid <= arr[i] - left:
      count += 1
      left = arr[i]

  if count >= c:
    ansMax = max(mid, ansMax)
    start = mid + 1
  else:
    end = mid
print(ansMax)