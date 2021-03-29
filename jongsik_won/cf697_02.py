import sys

T=int(sys.stdin.readline())

for _ in range(T):
    num=int(sys.stdin.readline())

    if(num%2020<=num//2020):
        print("YES")
    else:
        print("NO")