import sys

n=input()
nums=list(map(int,sys.stdin.readline().split()))
print("%d %d"%(min(nums),max(nums)))