import sys

T=int(sys.stdin.readline())

for _ in range(T):
    num=int(sys.stdin.readline())

    while(num%2==0):
        num=num//2
    
    if(num>1):
        print("YES")
    else:
        print("NO")
