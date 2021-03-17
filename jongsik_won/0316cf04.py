import sys


T=int(sys.stdin.readline())

def get_ans(s,e,nums,d):
    if(s>e):
        return []
    if s==e:
        return [d]
    m=0
    digit=0
    for i in range(s,e+1):
        if(nums[i]>m):
            m=nums[i]
            digit=i
    return get_ans(s,digit-1,nums,d+1)+[d]+get_ans(digit+1,e,nums,d+1)

for _ in range(T):
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    ans=get_ans(0,len(nums)-1,nums,0)
    for i in ans:
        print(i,end=" ")
    print()

