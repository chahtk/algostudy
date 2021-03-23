arr = list(map(int, input().split()))

total = [1,1,2,2,2,8]
ans = []

for i in range(len(arr)):
  print((total[i] - int(arr[i])), end=' ')
