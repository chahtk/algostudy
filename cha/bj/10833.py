n = int(input())

arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

ans = 0

for students, apples in arr:
  ans += apples%students

print(ans)