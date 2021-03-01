N=int(input())
A=list(map(int,input().split()))

c=0

AA=max(A)

b=[0]*N

for i in range(N):
    b[i]=A[i]/AA*100

for i in range(N):
    c = c+b[i]

print(c/N)