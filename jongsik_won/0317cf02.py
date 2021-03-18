import sys
T= int(sys.stdin.readline())

for _ in range(T):
    n=int(sys.stdin.readline())
    nums1=list(map(int,sys.stdin.readline().split()))
    nums2=list(map(int,sys.stdin.readline().split()))
    
    m1=min(nums1)
    m2=min(nums2)
    ans=0
    for i in range(n):
        ans+=max(nums1[i]-m1,nums2[i]-m2)
    print(ans)