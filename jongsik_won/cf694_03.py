import sys

T=int(sys.stdin.readline())





for _ in range(T):
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    ans=0
    for i in range(n-1,-1,-1):
        if(i+nums[i]<n):
            nums[i]=nums[i]+nums[i+nums[i]]
    print(max(nums))



