import sys

n=int(sys.stdin.readline())
nc=list(map(int,sys.stdin.readline().split()))

nc.sort()

m=int(sys.stdin.readline())
mc=list(map(int,sys.stdin.readline().split()))



for i in range(m):
    left=0
    right=n-1

    while left<=right:
        q=(left+right)//2
        qq=nc[q]

        if qq>mc[i]:
            right=q-1
            if right == -1:
                print(0,end=' ')
                break

        elif qq<mc[i]:
           left=q+1

        elif qq==mc[i]:
            print(1,end=' ')
            break

        if left>right:
            print(0,end=' ')
            break