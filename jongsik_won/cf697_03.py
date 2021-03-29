import sys

T=int(sys.stdin.readline())

for _ in range(T):
    a,b,k=map(int,sys.stdin.readline().split())
    boy=list(map(int,sys.stdin.readline().split()))
    girl=list(map(int,sys.stdin.readline().split()))
    ans=0
    bCount=[0 for _ in range(a+1)]
    gCount=[0 for _ in range(b+1)]
    for i in range(k):
        bCount[boy[i]]+=1  
        gCount[girl[i]]+=1
    ans=0
    for i in range(k):
        get=0
        get=k-bCount[boy[i]]-gCount[girl[i]]+1
        ans+=get
    print(ans//2)