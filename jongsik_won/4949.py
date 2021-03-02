import sys

while True :
    get=str(sys.stdin.readline())
    if get[0]=='.':
       break
    a=0
    b=0
    c=0
    for i in range(len(get)):
        if get[i]=='(':
            a+=1
        if get[i]==')':
            a-=1
            if(a<0):
                c=1
                print("no")
                break
        if get[i]=='[':
            b+=1
        if get[i]==']':
            b-=1
            if(b<0):
                c=1
                print("no")
                break
    if(a==0 and b==0):
        print("yes")
    elif c==0:
        print("no")


