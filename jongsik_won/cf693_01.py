import sys

T=int(sys.stdin.readline())

for _ in range(T):
    nums=list(map(int,sys.stdin.readline().split()))

    ans=1
    c=False
    while(nums[0]%2==0):
        ans*=2
        nums[0]=nums[0]//2
        if(ans>=nums[2]):
            c=True
            break

    while(nums[1]%2==0):
        if(c):
            break
        ans*=2
        nums[1]=nums[1]//2
        if(ans>=nums[2]):
            c=True
            break
    if(ans>=nums[2]):
        print("YES")
    else:
        print("NO")