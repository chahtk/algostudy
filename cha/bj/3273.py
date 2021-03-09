n = int(input())
arr = list(map(int, input().split()))
x = int(input())

res = 0
pA, pB = 0, 1

arr.sort()

while pA < len(arr)-1:
  sums = arr[pA] + arr[pB]
  if sums == x:
    res += 1
    pA += 1
    pB = pA + 1
    if pB == len(arr):
      break
    if arr[pA] + arr[pB] > x:
      break
    continue

  if pB + 1 < len(arr):
    pB += 1
  else:
    pA += 1
    pB = pA + 1
    if pB == len(arr):
      break
    if arr[pA] + arr[pB] > x:
      break

print(res)