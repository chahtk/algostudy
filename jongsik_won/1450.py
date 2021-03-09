import sys


n,w=map(int,sys.stdin.readline().split())

obj=list(map(int,sys.stdin.readline().split()))
obj.sort()

def get(now,rest):
    global w
    if(now==len(obj)-1 or obj[now]>w):
        if(rest<obj[now]):
           return 1
        else:
            return 2
    if(rest<obj[now]):
        return get(now+1,rest)
    else:
        return get(now+1,rest)+get(now+1,rest-obj[now])

print(get(0,w))