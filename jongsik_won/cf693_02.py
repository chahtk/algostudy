import sys

T=int(sys.stdin.readline())

for _ in range(T):
    n=sys.stdin.readline()
    nums=list(map(int,sys.stdin.readline().split()))
    c1=0
    c2=0
    s=sum(nums)
    if(s%2!=0):
        print("NO")
    else:
        for i in nums:
            if(i==1):
                c1+=1
            else:
                c2+=1
        if((c2%2)==0):
            print("YES")
        else:
            if(c1!=0):
                print("YES")
            else:
                print("NO")
        
    