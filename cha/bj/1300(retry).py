n = int(input())
k = int(input())

'''
n = 3
=====
1 2 3
2 4 6
3 6 9
'''

start, end = 1, k
while start < end:
  mid = (start+end) // 2
  count = 0
  for i in range(1, n+1):
    count += min(n, mid // i)
  if count < k:
    start = mid + 1
  else:
    end = mid
print(start)