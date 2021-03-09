import sys

block=[
       [[0],[0,0,0,0]],
       [[0,0]],
       [[0,0,-1],[0,1]],
       [[0,1,1],[0,-1]],
       [[0,0,0],[0,1],[0,1,0],[0,-1]],
       [[0,0,0],[0,0],[0,-1,-1],[0,2]],
       [[0,0,0],[0,-2],[0,0],[0,0,1]],
       ]

c,b_type=map(int,sys.stdin.readline().split())

base=list(map(int,sys.stdin.readline().split()))
b_type-=1
ans =0
for now in range(c) :
    for r in range(len(block[b_type])):
        check=True
        for l in range(len(block[b_type][r])):
            if(now+l>=c):
                check=False
                break
            else:
                if(base[now+l]+block[b_type][r][l]!=base[now]+block[b_type][r][0]):
                    check=False
                    break
        if(check):
            ans+=1

print(ans)
