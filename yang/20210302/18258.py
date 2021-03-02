a=[]

n=int(input())

for i in range(n):
    x=input().split()

    if x[0]=='push':
        a.append(x[1])
    elif x[0]=='pop':
        if len(x)==0:
            return -1
        else :
            return -1


    elif x[0]=='size':

    elif x[0]=='empyt':

    elif x[0]=='front':

    elif x[0]=='back':


print(x[2])
