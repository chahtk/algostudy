import sys


n=int(sys.stdin.readline())
k=int(sys.stdin.readline())


l=1
r=k

while l<r:
    mid=(l+r)//2
    count=0
    for i in range(1,n+1):
        count+=min(n,mid//i)  
    if (count>=k):
        r=mid
    elif (count<k):
        l=mid+1
print(l)