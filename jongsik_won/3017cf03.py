import sys
T=int(sys.stdin.readline())

for _ in range(T):
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    add=[0 for _ in range(2*n+1)]
    count=[0 for _ in range(n+1)]
    for i in nums:
        count[i]+=1
    for i in range(len(count)-1):
        add[i*2]+=count[i]//2
        for j in range(i+1,len(count)):
            add[i+j]+=min(count[i],count[j])
    add[n*2]+=count[n]//2
    print(max(add))