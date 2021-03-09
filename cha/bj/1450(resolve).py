[n, c] = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = 0

arrA = arr[:n//2]
arrB = arr[n//2:]

sumCombA = []
sumCombB = []

# search 'arr' and append to 'combArr' about value combination
def bruteSearch(arr, combArr, index, value):
  if index == len(arr):
    combArr.append(value)
    return
  
  # keep value
  bruteSearch(arr, combArr, index+1, value)
  # add value
  bruteSearch(arr, combArr, index+1, value+arr[index])

# sumCombArr : get all combinations about arrA, arrB
initIdx, initVal = 0, 0
bruteSearch(arrA, sumCombA, initIdx, initVal)
bruteSearch(arrB, sumCombB, initIdx, initVal)

sumCombA.sort()

# get index that 'keyVal' started in arr
def lowerBound(arr, keyVal):
  start, end = 0, len(arr)
  while start < end:
    mid = (start+end) // 2
    if arr[mid] > keyVal:
      end = mid
    else:
      start = mid + 1
  return end

for bEl in sumCombB:
  diff = c - bEl
  if diff < 0:
    continue
  ans += lowerBound(sumCombA, diff)

print(ans)