import sys

[n, c] = list(map(int, sys.stdin.readline().split()))
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

count = c
setted = []

def binarySearch(start, end):
  global count
  if count == 0 or start >= end or end>=len(arr):
    return

  mid = (start+end)//2
  tempMid = mid
  prev = 0
  prevMid = mid

  # arr [1 2 3 4 8 16]
  # s:0 , end:5, mid:2 => vlaue:3
  # leftdiff: 3-1, rightdiff: 16-3
  # => tempmid: 3 => 4
  # 8
  while True:
    flag = False
    leftDiff = arr[tempMid] - arr[start]
    rightDiff = arr[end-1] - arr[tempMid]
    if leftDiff < rightDiff:
      if prev < leftDiff:
        prev = leftDiff
        prevMid = tempMid
        tempMid += 1
        flag = True
    else:
      if prev < rightDiff:
        prev = rightDiff
        prevMid = tempMid
        tempMid -= 1
        flag = True
    if not flag:
      break

  mid = prevMid
  setted.append(arr[mid])
  count -= 1

  binarySearch(start, mid+1)
  binarySearch(mid+1, end)

setted.append(arr[0])
setted.append(arr[len(arr)-1])
count -= 2

binarySearch(0, len(arr))
setted.sort()

minDist = 1e9
for i in range(len(setted) -1):
  dist = setted[i+1] - setted[i]
  minDist = min(minDist, dist)
print(minDist)