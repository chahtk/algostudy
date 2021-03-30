import sys
k=int(input())
c=int(input())

for i in range(c):
    m,n=map(int,sys.stdin.readline().split())

    if m>n:
        kk=k-n
        mm=m-n
        if kk%2==0:
            kk=kk+1
        if kk-mm>=kk//2:
            print(1)
        else :
            print(0)
    elif m<n:
        kk=k-m
        nn=n-m
        if kk-nn>=kk//2:
            print(1)
        else :
            print(0)
    else:
        print(1)

    i+=1