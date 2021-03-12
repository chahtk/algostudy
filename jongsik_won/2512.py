import sys

n=sys.stdin.readline()

nums=list(map(int,sys.stdin.readline().split()))

total= int(sys.stdin.readline())

l=1
r=max(nums)
ans=0
if sum(nums)<=total:
    print(max(nums))
else:
    while l<r:
        mid=(l+r)//2
        add=0
        for i in nums:
            add+=min(i,mid)
        
        if(add<=total):
            l=mid+1
        else:
            ans=mid
            l=mid+1
    print(ans)
