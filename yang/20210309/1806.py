import sys
n,s=map(int,sys.stdin.readline().split())
k=list(map(int,sys.stdin.readline().split()))
count=1
rCount=0
rRCount=n
left=0
right=1
sSum=k[left]

while left<n:

    if sSum<s:
        if left==n or right==n:
            break
        else :
            sSum+=k[right]
            count+=1
            right+=1
            continue
    elif sSum>=s:
        rCount=count
        count=1
        left+=1
        right=left+1
        if k[n-1]>s:
            rRCount=1
            continue
        sSum=k[left]


    if rRCount>rCount:
        rRCount=rCount

if sum(k)<s:
    rRCount=0

print(rRCount)