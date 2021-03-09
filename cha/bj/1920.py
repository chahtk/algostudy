import sys

n = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()
res = []

def bs(left, right, x):
  ans = False
  mid = (left+right) // 2

  if right < left:
    return False
  
  if arr1[mid] == x:
    return True
  
  if arr1[mid] > x:
    ans = bs(left, mid-1, x)
  else:
    ans = bs(mid+1, right, x)
  
  return ans

for item in arr2:
  r = bs(0, len(arr1)-1, item)
  res.append(1 if r==True else 0)

for r in res:
  print(r)