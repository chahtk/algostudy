n=int(input())

def dp(k):
    x=[0]
    x.append(1)
    x.append(1)
    x.append(1)
    x.append(2)
    x.append(2)

    if k>5:
        for i in range(6,k+1):
            x.append(x[i-1]+x[i-5])
    return x[k]

for i in range(n):
    k=int(input())
    print(dp(k))