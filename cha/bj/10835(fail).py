n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
ans = 0

lIndex = 0
Rindex = 0
lMax = max(left)

while lIndex < n and Rindex < n:
  lMax = max(left[lIndex:]) # 남은 left 중 최대값
  if left[lIndex] > right[Rindex]: # right가 작을 때
    ans += right[Rindex]
    Rindex += 1
  elif lMax <= right[Rindex]: # left<=right 이고, 심지어 right가 lMax이상이다. 즉 사라져야할 카드.
    Rindex += 1
    lIndex += 1
  else: # left<=right지만, lMax이상은 아니므로 left를 버린다.
    lIndex += 1

print(ans)