from collections import deque
dq=deque()

n=list(map(int,input().split()))
print(n)

for i in range(n[1]):
    x=list(map(int,input().split()))
    dq.append(x)


print(dq)

