import sys

T=int(sys.stdin.readline())

for _ in range(T):
    a,b=map(int,sys.stdin.readline().split())

    blog=list(map(int,sys.stdin.readline().split()))
    count=[0 for _ in range(1001)]

    for i in blog:
        count[i]+=1
    ans=1
    for i in range(1000, -1, -1):
        if(b-count[i]<=0):
            for c in range(b):
                ans=(ans*(count[i]-c))//(c+1)     
            break
        b-=count[i]
    print(ans%1000000007)