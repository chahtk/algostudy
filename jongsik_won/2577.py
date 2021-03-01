import sys


nums=[0,0,0,0,0,0,0,0,0,0]
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
d=a*b*c
while(d>0) :
    t=d%10
    nums[int(t)]+=1    
    d=int(d/10)
for i in nums :
    print(i)

