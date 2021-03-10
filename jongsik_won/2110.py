import sys


N,C=map(int,sys.stdin.readline().split())
router=[]

for _ in range(N):
    get=int(sys.stdin.readline())
    router.append(get)

router.sort()

def check(l):
    c=1
    now=1
    before=0
    while(c<=C and now<N):
        if(router[before]+l<=router[now]):
            c+=1
            befor=now
        now+=1
    if(now>N):
        return 1
    if(c>C):
        return -1
    return 0

def binarySearch(l,r):
    mid=(l+r)/2
    if(check(mid)==0):
        print(mid)
        return 
    elif(check(mid)==1):
        binarySearch(l,mid-1)
    if(check(mid)==-1):
        binarySearch(mid+1,r)
        
binarySearch(router[0],router[len(router)-1])