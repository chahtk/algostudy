import sys
n,m,k=map(int,sys.stdin.readline().split())
arr=[0]*n

for i in range(n):
    arr[i]=int(input())


tree=[0]*n*4

def init(arr,tree,node,start,end):
    if start == end:
        tree[node-1]=start
    else:
        init(arr,tree,node*2,start,(start+end)//2)
        init(arr,tree,node*2+1,(start+end)//2+1,end)
        if arr[tree[node*2-1]]<arr[tree[node*2]]:
            tree[node-1]=tree[node*2-1]
        else:
            tree[node-1]=tree[node*2]


# def seg(arr,tree,node):


print(n+m)
print(arr)
# for i in range(n):
