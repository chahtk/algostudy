n=int(input())

x=[0]

def dp(k):
    x.append(1)
    x.append(3)

    for i in range(3,k+1):
        x.append((x[i-1]+x[i-2]*2))
    return x[k]

print(dp(n)%10007)