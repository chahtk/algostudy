T=int(input())
i=0
while i<T :
    a,b=map(int,input().split(" "))
    print("Case #%d: %d + %d = %d"%(i+1,a,b,a+b))
    i+=1 