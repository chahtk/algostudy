# n개의 물건, c 만큼의 무게를 넣을 수 있는 배낭
[n, c] = list(map(int, input().split()))
# 물건들의 무게
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, len(arr)-1
ans = 1
maxCount = 0
sumArr = sum(arr)

while True:
  if right < 0:
    break
  if sumArr <= c:
    maxCount = max(maxCount, right + 1) # 최대일 때, 각 원소를 하나씩 고를 때
    ans += 1 # 이 때의 전체 조합을 개수로 카운트
  sumArr -= arr[right]
  right -= 1
print(ans + maxCount)

'''
2 1
1 1
===
3

2 1
0 0
===
4
'''