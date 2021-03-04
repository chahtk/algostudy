import sys


T=int(sys.stdin.readline())

test=0
stack=[]
while test<T:
    get= int(sys.stdin.readline())
    if(get==0):
        stack.pop()
    else:
        stack.append(get)
    test+=1
print(sum(stack))