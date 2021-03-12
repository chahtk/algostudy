import sys

T=int(sys.stdin.readline())

for _ in range(T):
    a,b=map(int,sys.stdin.readline().split())
    ans=1
    for i in range(a):
        ans*=(b-i)
        ans/=(i+1)
    print(int(ans))
