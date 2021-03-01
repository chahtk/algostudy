n = input()
arr = list(map(int, input().split()))

sumNum = sum(arr)
maxNum = max(arr)
result = 0

for item in arr:
  result += (item/maxNum) * 100

print(round(result/len(arr), 6))