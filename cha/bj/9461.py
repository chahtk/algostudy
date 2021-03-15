arr = [-1] * 101
arr[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def dp():
  for i in range(11, 101):
    arr[i] = arr[i-1] + arr[i-5]
dp()

t = int(input())

for _ in range(t):
  n = int(input())
  print(arr[n])
