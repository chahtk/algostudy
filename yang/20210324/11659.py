import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

arr_sum=[0 for _ in range(n+1)]
for i in range(1,n+1):
    arr_sum[i]=arr_sum[i-1]+arr[i-1]

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    print(arr_sum[b]-arr_sum[a-1])