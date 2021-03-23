import sys
sys.setrecursionlimit(10000)

n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
ans = 0
dp = [[-1]*(n+1) for _ in range(n+1)]

def solve(l, r, s):
  if l == n or r == n:
    return
  # print(l, r, s ,'====  ', left[r], right[r])
  if left[l] > right[r]:
    if dp[l][r+1] == -1:
      dp[l][r+1] = s + right[r]
      solve(l, r+1, s+right[r])
  else:
    if dp[l+1][r] == -1:
      dp[l+1][r] = s
      solve(l+1, r, s)
    if dp[l+1][r+1] == -1:
      dp[l+1][r+1] = s
      solve(l+1,r+1, s)
solve(0,0,0)

for i in range(n+1):
  for j in range(n+1):
    ans = max(dp[i][j], ans)
print(ans)