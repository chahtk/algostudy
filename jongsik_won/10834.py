import sys

ans=1
r=True
N=int(sys.stdin.readline())
for _ in range(N):
    a,b,c=map(int,sys.stdin.readline().split())
    if(c==1):
        r=not r
    ans=int(ans*b/a)

if(r):
    print(0,ans)
else:
    print(1,ans)

