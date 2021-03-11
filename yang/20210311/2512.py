import sys
n=int(input())
k=list(map(int,sys.stdin.readline().split()))
x=int(input())
y=x//n
left=0

k.sort()

for i in range(n):
    if k[i]<=y:
        x-=k[i]
    else :
        left=i
        break



while k[left]<y:
    y=x//(n-left+1)
    for i in range(left,n):
        if k[i]<=y:
            x-=k[i]
        else :
            left=i
            break


y=x//(n-left)

print(y)