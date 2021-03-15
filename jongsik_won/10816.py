import sys

get=sys.stdin.readline()

nums=list(map(int,sys.stdin.readline().split()))

nums.sort()

get=sys.stdin.readline()

cal=list(map(int,sys.stdin.readline().split()))

def func(target):
    l=0
    r=len(nums)
    l_ans=0
    check=False
    while(l<r):
        mid=(l+r)//2
        if(nums[mid]==target):
            check=True
        if(nums[mid]<target):
            l=mid+1
        else:
            r=mid
    if(check==False):
        return 0
        
    l_ans=l
    l=0
    r=len(nums)
    check=False
    while(l<r):
        mid=(l+r)//2
        if(nums[mid]==target):
            check=True
        if(nums[mid]<=target):
            l=mid+1
        else:
            r=mid
    return l-l_ans

for i in cal:
    print(func(i),end=" ")