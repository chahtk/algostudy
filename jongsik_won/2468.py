import sys
from collections import deque


N=int(sys.stdin.readline())

height=[[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    height[i]=list(map(int,sys.stdin.readline().split()))

max=0
min=100
for i in range(N):
    for j in range(N):
        if(max<height[i][j]):
            max=height[i][j]
        if(min>height[i][j]):
            min=height[i][j]

ans=0
for now in range(min,max):
    count=0
    temp=[[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if(height[i][j]>now):
                temp[i][j]=height[i][j]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(N):
        for j in range(N):
            if(temp[i][j]>0):
                count+=1
                que=deque()
                que.append([i,j])
                temp[i][j]=0
                while(len(que)!=0):
                    n=que.pop()
                    for d in range(4):
                        nx=n[0]+dx[d]
                        ny=n[1]+dy[d]
                        if(0<=nx<N and 0<=ny<N):
                            if(temp[nx][ny]!=0):
                                que.append([nx,ny])
                                temp[nx][ny]=0
    if(ans<count):
        ans=count
if(min==max):
    print(1)
else:
    print(ans)