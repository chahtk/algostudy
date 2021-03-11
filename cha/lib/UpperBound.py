arr = [5,2,3,7,8]

def UpperBound(arr, key):
  # 키 값 이하 중 최대 값 찾는 함수
  start, end = 0, len(arr)
  while start < end:
    mid = (start+end)//2
    if arr[mid] > key:
      end = mid
    else:
      start = mid + 1
  print(arr[start-1])

arr.sort()
print(arr)
# UpperBound(arr, 5)

# 6을돌리면 7, 5를 돌리면? 5가 나오는 함수를 구현
def func2(arr, key):
  start, end = 0, len(arr)
  while start<end:
    mid = (start+end)//2
    if arr[mid] < key:
      start = mid + 1
    else:
      end = mid
  print(arr[start])

func2(arr, 6)
func2(arr, 5)
