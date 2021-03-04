import sys



T=int(sys.stdin.readline())

stack=[]
for i in range(T):
    get=list(map(str,sys.stdin.readline()))
    if(get[0]=='push'):
        stack.append(get[1])
    elif(get[0]=='pop'):
        if(len(stack)!=0):
            print(stack[0])
            del stack[0]
        else:
            print(-1)
    elif(get[0]=='size'):
        print(len(stack))
    elif(get[0]=='empty'):
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    elif(get[0]=='front'):
        if(len(stack)!=0):
            print(stack[0])
        else:
            print(-1)
    elif(get[0]=='back'):
        if(len(stack)!=0):
            print(stack[len(stack)-1])
        else:
            print(-1)