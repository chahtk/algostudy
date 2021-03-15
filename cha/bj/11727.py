n = int(input())

if n == 1 or n == 2:
  print(1 if n==1 else 3)
  exit()

dp = [-1] * (n+1)

dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
  dp[i] = (dp[i-1] + (dp[i-2] * 2)) % 10007

print(dp[n])

''' TOP-DOWN 방식은 시간 초과 '''
# def dpFunc(n):
#   x, y = dp[n-1], dp[n-2]
#   if x == -1:
#     x = dpFunc(n-1)
#   if y == -1:
#     y = dpFunc(n-2)
#   return (x + y * 2) % 10007

# print(dpFunc(n))