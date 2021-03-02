n=input()
y=list(map(int,input().split()))
x=list(map(int,input().split()))
k=0
xx=x[0]

for i in range(len(x)-1):
    if xx>x[i]:
        xx=x[i]

    k=k+xx*y[i]

print(k)