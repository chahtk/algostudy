n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

cards.sort()

def binarySearch(arr, x):
  start, end = 0, len(arr)
  while start < end:
    mid = (start+end)//2
    if arr[mid] == x:
      return True
    if arr[mid] > x:
      end = mid
    else:
      start = mid+1
  return False
ans = []
for target in targets:
  res = binarySearch(cards, target)
  ans.append(res)

for a in ans:
  print('%d '%1 if a else '%d '%0, end='')