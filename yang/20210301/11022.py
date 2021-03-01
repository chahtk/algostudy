T=int(input())
i=T

while T > 0:
    T -= 1
    A,B=map(int,input().split())
    print("Case #%d: %d + %d = %d"%(i-T,A,B,A+B))