import sys

m,d=map(int,sys.stdin.readline().split())

dp=[[[1 for _ in range(2)]for _ in range(m)]for _ in range(m)]

get=[0 for i in range(2*m-1)]


# for _ in range(d):
#     a,b,c=map(int,sys.stdin.readline().split())
#     add=[0 for _ in range(a)]+[1 for _ in range(b)]+[2 for _ in range(c)]
#     for i in range(2*m-1):
#         get[i]+=add[i]

for i in range(m):
    dp[m-1-i][0][0]=get[i]
    dp[m-1-i][0][1]+=dp[m-1-i][0][0]
for i in range(1,m):
    dp[0][0+i][0]=get[m-1+i]   
    dp[0][0+i][1]+=dp[0][0+i][0]
for i in range (1,m):
    for j in range(1,m):
        dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j-1][0],dp[i][j-1][0])
        dp[i][j][1]+=dp[i][j][0]


for i in range(m):
    for j in range(m):
        print(dp[i][j][1],end=" ")
    print()