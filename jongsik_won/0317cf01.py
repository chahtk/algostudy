import sys

T=int(sys.stdin.readline())

for _ in range(T):
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))

    nums.sort()
    c=True
    for i in range(len(nums)-1):
        if(nums[i+1]-nums[i]>1):
            print("NO")
            c=False
            break
    if(c):
        print("YES")