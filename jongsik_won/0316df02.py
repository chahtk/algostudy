import sys

T=int(sys.stdin.readline())


for _ in range(T):
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    
    count=[0,0,0]
    for i in nums:
        count[i%3]+=1
    for i in range(3):
        count[i]=int(count[i]-n/3)
#    count=list(map(int,sys.stdin.readline().split()))        
    ans=0
    for i in range(3):
        if(count[i]>0):
            ans+=count[i]
            count[(i+1)%3]+=count[i]
            if(count[(i+1)%3]>0):
                ans+=count[(i+1)%3]
            else:
                ans+=-2*count[(i+1)%3]
            break
    print(int(ans))