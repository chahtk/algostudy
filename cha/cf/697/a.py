t = int(input())
res = []

for _ in range(t):
  n = int(input())
  
  if n % 2 == 1:
    res.append('YES')
    continue
  
  tempN = n // 2
  flag = True
  while tempN > 2:
    if tempN % 2 == 1:
      res.append('YES')
      flag = False
      break
    tempN = tempN // 2
  
  if flag:
    res.append('NO')

for r in res:
  print(r)