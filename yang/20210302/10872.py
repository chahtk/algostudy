n=int(input())

def f(n):
    if n==0:
        return 1
    elif n==1:
        return 1

    return f(n-1)*n


print(f(n))