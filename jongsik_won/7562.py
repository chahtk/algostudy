import sys
from queue import Queue
from collections import deque

Test=int(sys.stdin.readline())

for _ in range(Test):
    size=int(sys.stdin.readline())
    visit=[[0]*size for i in range(size)]
    s_x,s_y=map(int,sys.stdin.readline().split())
    e_x,e_y=map(int,sys.stdin.readline().split())
    que=deque()
    
    que.append([s_x,s_y,0])
    visit[s_x][s_y]=1
    dx=[-1, -2, -2, -1, 1, 2, 2, 1]
    dy=[-2, -1, 1, 2, -2, -1, 1, 2]
    while(len(que)!=0):
        now=que.popleft()
        if(now[0]==e_x and now[1]==e_y):
            print(now[2])
            break
        for i in range(8):
            n_x=now[0]+dx[i]
            n_y=now[1]+dy[i]
            if(0<=n_x<size and 0<=n_y<size):
                if(visit[n_x][n_y]==0):
                    que.append([n_x,n_y,now[2]+1])
                    visit[n_x][n_y]=1
 