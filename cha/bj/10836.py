[m, n] = list(map(int, input().split()))

growing = []
arr = [[1]*m for _ in range(m)]

for _ in range(n):
  growing.append(list(map(int, input().split())))

totalGrow = [0] * (2*m-1)

for day in range(n):
  grow = growing[day][0] * [0] + growing[day][1] * [1] + growing[day][2] * [2]
  for i in range(2*m-1):
    totalGrow[i] += grow[i]

# init
dp = [[0]*m for _ in range(m)] # 0, 1, 2
for i in range(m-1, 2*m-1):
  dp[0][i-(m-1)] = totalGrow[i]
for i in range(0, m-1):
  dp[m-i-1][0] = totalGrow[i]

for i in range(1, m):
  for j in range(1, m):
    maxGrow = max(dp[i-1][j], dp[i][j-1])
    maxGrow = max(dp[i-1][j-1], maxGrow)
    dp[i][j] = maxGrow

for i in range(m):
  for j in range(m):
    arr[i][j] += dp[i][j]

for row in arr:
  for col in row:
    print(col, end=' ')
  print()