import sys

N=int(sys.stdin.readline())

dp=[[[0 for _ in range(1024)] for _ in range(10)] for _ in range(101)]

for i in range(1,10):
    dp[1][i][1<<i]=1


for i in range(2,N+1):
    for d in range(1024):
        dp[i][0][d|1<<0]+=dp[i-1][1][d]
        dp[i][0][d|1<<0]%=1000000000
        for n in range(1,9):
            dp[i][n][d|1<<n]+=dp[i-1][n-1][d]
            dp[i][n][d|1<<n]+=dp[i-1][n+1][d]
            dp[i][n][d|1<<n]%=1000000000
        dp[i][9][d|1<<9]+=dp[i-1][8][d]
        dp[i][9][d|1<<9]%=1000000000
                          
ans=0
for i in range(10):
    ans+=dp[N][i][1023]
    print(dp[N][i][1023])
print(ans)