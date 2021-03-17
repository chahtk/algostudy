t = int(input())

dp = [0] * (int(1e4)+1)
for i in range(1, int(1e4) +1):
  dp[i] = pow(i,3)

def solve(x):
  for a in range(1,int(1e4)+1):
    if dp[a] > x:
      break

    left, right = 1, len(dp)
    while left < right:
      mid = (left + right) // 2
      if dp[mid] + dp[a] == x:
        return True
      if dp[mid] + dp[a] > x:
        right = mid
      else:
        left = mid + 1
    # if dp[right] == x:
    #   return True
  return False
for _ in range(t):
  x = int(input())
  if solve(x):
    print('YES')
    continue
  print('NO')