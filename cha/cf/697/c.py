import sys
t = int(sys.stdin.readline())

for _ in range(t):
  a,b,k = map(int, sys.stdin.readline().split())
  boys = list(map(int, sys.stdin.readline().split()))
  girls = list(map(int, sys.stdin.readline().split()))
  
  dpBoy = [0] * (a+1)
  dpGirl = [0] * (b+1)

  for i in range(k):
    dpBoy[boys[i]] += 1
    dpGirl[girls[i]] += 1
  
  count = 0
  for i in range(k):
    dpB, dpG = dpBoy[boys[i]], dpGirl[girls[i]]
    count += k - dpB - dpG + 1
  print(count//2)