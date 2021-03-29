import sys

while True :

    k=0
    a=0
    b=0
    c=0
    d=0

    n=(sys.stdin.readline().rstrip("\n"))

    if not n:
        break

    while k<len(n):
        if n[k].islower():
            a+=1
        elif n[k].isupper():
            b+=1
        elif n[k].isdigit():
            c+=1
        elif n[k].isspace():
            d+=1
        k+=1


    print(a,b,c,d)