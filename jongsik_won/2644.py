import sys

people=int(sys.stdin.readline())

chon=[[] for _ in range(people+1)]

a,b=map(int,sys.stdin.readline().split())

c=int(sys.stdin.readline())
for _ in range(c):
    g1,g2=map(int,sys.stdin.readline().split()) 
    chon[g1].append(g2)
    chon[g2].append(g1)
visit=[0 for _ in range(people+1)]

ans=-1
def dfs(now,chonsu):
    global ans
    visit[now]=1
    if(now==b):
        print(chonsu)
        ans=chonsu
        return 0
    for i in range(len(chon[now])):
        if(visit[chon[now][i]]==0):
            dfs(chon[now][i],chonsu+1)
dfs(a,0)
print(ans)