import math

[n, k] = map(int, input().split())
students = [ [0, 0] for _ in range(7)]

for _ in range(n):
  [sex, year] = map(int, input().split())
  students[year][sex] += 1

room = 0

for y in range(1, 7):
  room += math.ceil(students[y][0]/k)
  room += math.ceil(students[y][1]/k)
print(room)