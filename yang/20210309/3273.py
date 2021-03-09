import sys
n=int(sys.stdin.readline())
k=list(map(int,sys.stdin.readline().split()))
x=int(sys.stdin.readline())
k.sort()
count=0
left=0
right=len(k)-1

while left<right:
    tmp=k[left]+k[right]
    if tmp == x :
        count += 1

    if tmp < x :
        left += 1
        continue

    right -= 1

print(count)