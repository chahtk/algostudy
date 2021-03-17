import sys

T=int(sys.stdin.readline())


for _ in range(T):
    ans=0
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))

    for i in range(len(nums)-1):
        b=max(nums[i],nums[i+1])
        s=min(nums[i],nums[i+1])
        if(b>2*s):
            temp=s
            while(2*temp<b):
                ans+=1
                temp*=2
    print(ans)
