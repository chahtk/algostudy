t = int(input())
res = []

for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  balancedNumber = n // 3
  c = [0] * 3

  for el in arr:
    c[el%3] += 1
  
  count = 0
  while max(c) > balancedNumber:
    for i in range(3):
      while c[i] > balancedNumber:
        c[i] -= 1
        if i+1 < 3:
          c[i+1] += 1
        else:
          c[0] += 1
        count += 1
  res.append(count)

for r in res:
  print(r)

'''
4
6
0 2 5 5 4 8
6
2 0 2 1 0 0
9
7 1 3 4 2 10 3 9 6
6
0 1 2 3 4 5
'''