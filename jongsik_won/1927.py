import sys
import heapq

heap=[]
res=[]
T=int(sys.stdin.readline())

for i in range(T):
    get=int(sys.stdin.readline())
    if(get==0):
        if(len(heap)!=0):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,get)