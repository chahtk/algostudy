import sys
n,m=map(int,sys.stdin.readline().split())
k=list(map(int,sys.stdin.readline().split()))
a=0
maxa=0

for j in range(m):
    a+=k[j]

maxa=a

for i in range(len(k)-m):
    
    if m==1:
        print(max(k))
        exit()
    else:
        a-=k[i]
        a+=k[i+m]
        if a>maxa:
            maxa=a

print(maxa)