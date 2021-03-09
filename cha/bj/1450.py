# 모든 경우의 수를 찾아 sum 배열을 채우는 함수
def bruteSearch(arr, sumArr, index, weight):
  if index >= len(arr):
    sumArr.append(weight)
    return None
  bruteSearch(arr, sumArr, index+1, weight)
  bruteSearch(arr, sumArr, index+1, weight + arr[index])
  # 0,0 -> bs(1,0),bs(1,arr[0])
  # bs(1,0) -> bs(2,0), bs(2, arr[1])
  # 즉, weight = 0 으로부터 모든 arr[index]가 파생될 수 있고
  # 마찬가지로, weight = arr[1] 로부터 모든 arr[1:index]가 파생될 수 있다.
  # 이런 식으로 모든 조합을 얻을 수 있다.

# input
[n, c] = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = 0

# split group
halfLen = n//2
arrA = arr[:halfLen]
arrB = arr[halfLen:]

# 각 배열에서 고를 수 있는 무게의 모든 경우의 수
sumA = []
sumB = []

# get sumArray(sumA, sumB)
initialWeight = 0
initialIndex = 0
bruteSearch(arrA, sumA, initialIndex, initialWeight)
bruteSearch(arrB, sumB, initialIndex, initialWeight)

# sort one group
sumA.sort()

# define solve [lower bound]
def lowerBound(arr, key):
  start, end = 0, len(arr)
  while start < end:
    mid = (start + end)//2
    if arr[mid] > key:
      end = mid
    else:
      start = mid + 1
  return end

# A X B
for bItem in sumB:
  diff = c - bItem
  if diff < 0:
    continue
  '''
  이 문제에서 lowerBound는 diff 값 이상의 인덱스를 리턴하는데,
  그 미만의 인덱스의 값들이 사실상 가능한 무게들이다.
  리턴 값 미만의 인덱스 개수 = 리턴 값 이므로,
  bItem과 가능한 조합의 수는 리턴 값이 된다.
  '''
  LBI = lowerBound(sumA, diff)
  ans += LBI

print(ans)
'''
2 1
1 1
===
3 // 0, 1, 1

2 1
0 0
===
4 // none, arr[0], arr[1], arr[0] + arr[1]

3 3
1 3 2
===
8 // none, arr[0], arr[1], arr[2], a[0]+a[2]
'''