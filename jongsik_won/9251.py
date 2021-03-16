import sys



str1=sys.stdin.readline()
str2=sys.stdin.readline()

dp=[[0 for i in range(1002)]for j in range(1002)]

for i in range(len(str1)-1):
    for j in range(len(str2)-1):
        if(str1[i]==str2[j]):
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])

print(dp[len(str1)-1][len(str2)-1])
print(len(str1),len(str2))
print(str1,end="")
print(str2,end="")