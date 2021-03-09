def lowBound(arr, key):
  start, end = 0, len(arr)
  while start < end:
    mid = (start+end) // 2
    if arr[mid] >= key:
      end = mid
    else:
      start = mid + 1
  return end

print(lowBound([1,2,4,6,8], 4)) # 2
print(lowBound([1,2,3,6,8], 4)) # 3
