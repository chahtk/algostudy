import sys

T=int(sys.stdin.readline())

dp=[0 for i in range(101)]

dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=2
for i in range(6,101):
    dp[i]=dp[i-1]+dp[i-5]


for _ in range(T):
    n=int(sys.stdin.readline())
    print(dp[n])
