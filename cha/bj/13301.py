n = int(input())

total = [0] * 81
length = [0] * 81

length[1] = 1
total[1] = 4

for i in range(2, n+1):
  length[i] = length[i-1] + length[i-2]
  total[i] = total[i-1] + length[i]*2

print(total[n])