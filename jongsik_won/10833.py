import sys

N=int(sys.stdin.readline())

ans=0
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    ans+=b%a

print(ans)