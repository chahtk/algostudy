import sys
n=int(input())
nc=list(map(int,sys.stdin.readline().split()))
m=int(input())
mc=list(map(int,sys.stdin.readline().split()))

nc.sort()

def by(k):
    left=0
    right=n

    while left<right:
        mid=(left+right)//2

        if nc[mid] >= k:
            right=mid
        else :
            left=mid+1

    return left

for a in mc:
    print(by(a+1)-by(a),end=' ')