import heapq as h
import sys
a=[]
k=0
q=0
n=int(sys.stdin.readline())

for i in range(n):
    k=int(sys.stdin.readline())
    if k==0:
        if len(a)==0:
            print(0)
        else :
            q=h.heappop(a)
            print(q)
    else :
        h.heappush(a,k)