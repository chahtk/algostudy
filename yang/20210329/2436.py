# import sys
# n,m=map(int,sys.stdin.readline().split())
# if m%n!=0 or n==0 or m==0:
#     exit()


# if n==m:
#     a=n
#     b=n
# else:
#     a=int(m/n)
#     k=a/n
#     b=int(m/k)

# if m!=(a//n)*(b//n)*n:
#     exit()

# if a>b:
#     temp=a
#     a=b
#     b=temp

# print(a,b)

def gcd(a,b):
    while b:
        mod = b
        b=a%b
        a=mod
    return a

g, l = map(int,input().split())
div = l//g
a,b=1,div
for i in range(1,div//2+1):
    if div%i ==0:
        c=i
        d=div//i
        if gcd(c,d) != 1:
            continue
        if a+b>c+d:
            a=c
            b=d
print(a*g,b*g)