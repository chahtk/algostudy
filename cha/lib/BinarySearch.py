def bs(arr, left, right, x):
  ans = False
  mid = (left+right) // 2

  if right < left:
    return False
  
  if arr[mid] == x:
    return True
  
  if arr[mid] > x:
    ans = bs(arr, left, mid-1, x)
  else:
    ans = bs(arr, mid+1, right, x)
  
  return ans
