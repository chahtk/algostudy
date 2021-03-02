import sys



def fibo(n) :
    if(n==1 or n==0):
        return 1
    return fibo(n-1)*n


get=int(sys.stdin.readline())

print(fibo(get))