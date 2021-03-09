[n, s] = list(map(int, input().split()))
arr = list(map(int, input().split()))

MAX = 1e9 + 19
ans = MAX
left, right, sumX = 0, 0, 0

while True:
  if sumX >= s:
    ans = min(ans, right-left)
    if ans == 1:
      break
    sumX -= arr[left]
    left += 1
  elif right == n:
    break
  else:
    sumX += arr[right]
    right += 1

print(ans if ans != MAX else 0)
