n = int(input())
arr = list(map(int, input().split()))
maxAmount = int(input())

arr.sort()

if sum(arr) <= maxAmount:
  print(arr[-1])
  exit()

def solve():
  start, end = 1, arr[-1]
  if start == end:
    print(start//len(arr))
    return
  while start <= end:
    mid = (start+end)//2
    tempSum = 0
    for val in arr:
      if mid > val:
        tempSum += val
      else:
        tempSum += mid

    if tempSum > maxAmount:
      end = mid - 1
    else:
      start = mid + 1
  print(end)

solve()

'''
s e m x
------- (while: s<e)
2 6 4 5 (if m<x)
5 6 5 5 (s=m+1)
5 5 5 5 (e=m)

2 6 4 4 (if m>=x, e=m)
2 4 3 4 (e=m, m<x)
4 4 4 4 (s=m+1)
'''

'''
4
120 110 140 150
485
=====
127

3
100 100 100
50
===
33

3
1 2 3
5
==
2
'''
