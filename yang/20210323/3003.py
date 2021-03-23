import sys
n=list(map(int,sys.stdin.readline().split()))
m=[1,1,2,2,2,8]
k=[m[0]-n[0],m[1]-n[1],m[2]-n[2],m[3]-n[3],m[4]-n[4],m[5]-n[5]]
x=0

for i in k:
    print(i,end=' ')