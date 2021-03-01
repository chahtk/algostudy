A=int(input())
B=int(input())
C=int(input())
k=A*B*C

k0=0
k1=0
k2=0
k3=0
k4=0
k5=0
k6=0
k7=0
k8=0
k9=0

a=[]

for i in str(k):
    a.append(i)
    if i == '0':
        k0 += 1
    elif i == '1':
        k1 +=1
    elif i == '2':
        k2 +=1
    elif i == '3':
        k3 +=1
    elif i == '4':
        k4 +=1
    elif i == '5':
        k5 +=1
    elif i == '6':
        k6 +=1
    elif i == '7':
        k7 +=1
    elif i == '8':
        k8 +=1
    elif i == '9':
        k9 +=1


print(k0)
print(k1)
print(k2)
print(k3)
print(k4)
print(k5)
print(k6)
print(k7)
print(k8)
print(k9)







