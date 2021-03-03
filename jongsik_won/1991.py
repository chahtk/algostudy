import sys
from typing import Dict


T=int(sys.stdin.readline())


a=[['.']*2 for i in range (26)]

def before(now):
    ans=chr(now+65)
    if(a[now][0]!='.') :
        ans+=before(ord(a[now][0])-65)
    if(a[now][1]!='.') :
        ans+=before(ord(a[now][1])-65)
    return ans

def mid(now):
    ans=''
    if(a[now][0]!='.') :
        ans+=mid(ord(a[now][0])-65)
    ans+=chr(now+65)
    if(a[now][1]!='.') :
        ans+=mid(ord(a[now][1])-65)
    return ans

def after(now):
    ans=''
    if(a[now][0]!='.') :
        ans+=after(ord(a[now][0])-65)
    if(a[now][1]!='.') :
        ans+=after(ord(a[now][1])-65)
    ans+=chr(now+65)
    return ans

for i in range(T):
    gets=list(map(str,sys.stdin.readline().split()))
    a[ord(gets[0])-65][0]=gets[1]
    a[ord(gets[0])-65][1]=gets[2]

print(before(0))
print(mid(0))
print(after(0))
