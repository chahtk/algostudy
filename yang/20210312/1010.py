import sys

n=int(input())
x=[0]
pp=0

def p(k):
        x.append(1)
        for i in range(2,k+1):
            x.append(x[i-1]*i)
        return x[k]

for i in range(n):
    k=list(map(int,sys.stdin.readline().split()))
    if k[0]==k[1]:
        pp=1
    else :
        pp=(p(k[1])/(p(k[1]-k[0])*p(k[0])))
        
    print(pp)

