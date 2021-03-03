import sys


count=[6,2,5,5,4,5,6,3,7,5,6]


ans=[]
total=0


def get_ans(get_s,left,sum) :
    if left==0 :
        if sum==total:
            ans.append(get_s)
        return 0
    for i in count :
        if sum+count[i]<total:
            get_ans(get_s+str(i),left-1,sum+count[i])
    return 0


g=str(sys.stdin.readline())

for i in range(len(g)-1):
    total+=count[int(g[i])]

get_ans('',len(g)-1,0)
print(ans)