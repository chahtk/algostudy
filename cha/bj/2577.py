a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)

arr = [0] * 10
for i in range(len(num)):
  arr[int(num[i])] += 1

for item in arr:
  print(item)

# count 함수
# for i in range(10):
#   print(num.count(str(i)))