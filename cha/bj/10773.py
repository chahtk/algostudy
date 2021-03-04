k = int(input())
arr = []

for _ in range(k):
  x = int(input())
  if x == 0 and len(arr) > 0:
    arr.pop()
  else:
    arr.append(x)

print(sum(arr))