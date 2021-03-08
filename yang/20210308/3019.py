import sys
from collections import deque

c,p=map(int,sys.stdin.readline().split())

ground=list(map(int,sys.stdin.readline().split()))


print(ground[2])

block=[
    [[0],[0,0,0,0]],
    [[0,0]],
    [[0,0,-1],[0,1]],
    [[0,1,1],[0,-1]],
    [[0,0,0],[0,1],[0,1,0],[0,-1]],
    [[0,0,0],[0,2],[0,-1,-1],[0,0]],
    [[0,0,0],[0,0],[0,0,1],[0,-2]]
]


block[p]