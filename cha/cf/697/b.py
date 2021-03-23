t = int(input())

dp = [0] * (int(1e6)+1)
def makeDP(num):
  if int(1e6) < num:
    return
  if dp[num] == 1:
    return
  dp[num] = 1
  makeDP(num + 2020)
  makeDP(num + 2021)

makeDP(0)
res = []

for _ in range(t):
  n = int(input())
  
  if dp[n] == 1:
    res.append('YES')
    continue
  res.append('NO')

for r in res:
  print(r)