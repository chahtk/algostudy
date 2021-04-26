n = input()
newLen = (len(n)-1)//3 # 0, 1, ...
ans = ''

cnt = 0
tempSum = 0

for i in range(len(n)-1, -1, -1):
  tempSum += int(n[i]) * int(pow(2,cnt))
  cnt += 1
  if cnt % 3 == 0:
    ans = str(tempSum) + ans
    cnt = 0
    tempSum = 0
if cnt != 0:
  ans = str(tempSum) + ans
print(ans)