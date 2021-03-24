a, b = input().split()
aa, bb = 0, 0
for i in range(3):
  aa += int(a[2-i]) * pow(10, 2-i)
  bb += int(b[2-i]) * pow(10, 2-i)

print(max(aa,bb))