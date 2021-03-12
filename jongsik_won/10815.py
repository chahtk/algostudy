import sys

get=sys.stdin.readline()

mine=list(map(int,sys.stdin.readline().split()))

mine.sort()

get=sys.stdin.readline()

gets=list(map(int,sys.stdin.readline().split()))

def binarySearch(l,r,t):
    if(l>r):
        return 0
    
    mid=(l+r)//2
    if(mine[mid]==t):
        return 1
    elif(mine[mid]>t):
        return binarySearch(l,mid-1,t)
    else:
        return binarySearch(mid+1,r,t)
    
for i in gets:
    print(binarySearch(0,len(mine)-1,i),end=" ")
    # if i in mine:
    #     print(1,end=" ")
    # else:
    #     print(0,end=" ")