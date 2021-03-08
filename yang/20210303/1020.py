import sys

k=input()

qq=list(k)

q=list(map(int,qq))

w=0

print(k)
print(q)

for i in range(len(q)):
    if q[i]==0:
        w+=6
    elif q[i]==1:
        w+=2
    elif q[i]==2:
        w+=5
    elif q[i]==3:
        w+=5
    elif q[i]==4:
        w+=4
    elif q[i]==5:
        w+=5
    elif q[i]==6:
        w+=6
    elif q[i]==7:
        w+=3
    elif q[i]==8:
        w+=7
    elif q[i]==9:
        w+=5

print(w)


