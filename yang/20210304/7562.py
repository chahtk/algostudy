a=[]
b=[]
aa=0
bb=0
k=0

x=list(map(int,input().split()))
a.append(x)
y=list(map(int,input().split()))
b.append(y)


aa=abs(a[0][0]-b[0][0])

bb=abs(a[0][1]-b[0][1])



# if aa>bb:
#     if aa%2==0:
#         if bb%2==0:
#             k=aa/2+(bb-aa/2)
    
#     elif aa%2==1:


    



# if aa==0 and bb==0:
#     k=0


print(a)
print(b)

print(aa)
print(bb)