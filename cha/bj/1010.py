t = int(input())
MAX = 31
factoArr = [-1] * MAX

def factoFunc(n):
  factoArr[0:2] = [1,1]
  for i in range(2, n+1):
    factoArr[i] = i * factoArr[i-1]

def combination(n,m):
  return factoArr[m] // (factoArr[m-n] * factoArr[n])

factoFunc(MAX-1)

for _ in range(t):
  [n, m] = list(map(int, input().split()))
  print((combination(n, m)))