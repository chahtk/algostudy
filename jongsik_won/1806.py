import sys


t,add=map(int,sys.stdin.readline().split())

p1=0
p2=0

nums=list(map(int,sys.stdin.readline().split()))

ans=-1
sum_nums=nums[0]
out=False
while (True) :
    while(sum_nums<add):
        p2+=1
        if(p2==len(nums)):
            out=True
            break
        sum_nums+=nums[p2]
  
    if(out):
        break
    while(True):
        if(sum_nums-nums[p1]>=add):
            sum_nums-=nums[p1]
            p1+=1
        else:
            if(ans==-1):
                ans=p2-p1
                if(p1+1<len(nums)):
                    sum_nums=nums[p1+1]
                else:
                    out=True
                p2=p1=p1+1
                break
            else:
                if(ans>p2-p1):
                    ans=p2-p1
                if(p1+1<len(nums)):
                    sum_nums=nums[p1+1]
                else:
                    out=True
                p2=p1=p1+1
                break
print(ans+1)

