import sys


cal=int(sys.stdin.readline())

bit=1
ans=0
for i in range(7):
    if cal&bit>0:
        ans+=1
    bit*=2
print(ans)
