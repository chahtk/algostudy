import sys

T=int(sys.stdin.readline())


mul=[0 for _ in range(10001)]

for i in range(1,10001):
    mul[i]=i*i*i

for _ in range(T):
    num=int(sys.stdin.readline())
    c=True
    for i in range(1,10001):
        if(mul[i]<=num/2):
            l=i
            r=10001
            while(l<=r):
                mid=(l+r)//2
                if(mul[i]+mul[mid]==num):
                    print("yes")
                    c=False
                    break
                if(mul[i]+mul[mid]<num):
                    l=mid+1
                if(mul[i]+mul[mid]>num):
                    r=mid-1
        else:
            break
    if(c):
        print("no")
                