# arr[자리][끝나는수][비트마스크]
# 012 를 체크한다고 하자. 이때 비트마스크의 값은 '111' 이 될 것이다. 즉, 7.
# arr[3-1][2][7] = 1
# answer를 찾을 때 비트마스크의 최대값(1<<10)

bitMask = 1<<10 # 1024
nMax = 100
mod = 1000000000

n = int(input())

arr = [[[0]*bitMask for _ in range(10)] for _ in range(n)]
# arr[layer][val][bit]

for layer in range(n):
  for val in range(10):
    if layer == 0:
      if val > 0:
        arr[layer][val][1<<val] = 1
      continue
    # layer >= 1
    for bit in range(bitMask):
      if val - 1 >= 0:
        arr[layer][val][bit|1<<val] = (arr[layer][val][bit|1<<val] + arr[layer-1][val-1][bit]) % mod
      if val + 1 < 10:
        arr[layer][val][bit|1<<val] = (arr[layer][val][bit|1<<val] + arr[layer-1][val+1][bit]) % mod
        # 001(0) 010(1) => 011
ansMax = 0
for i in range(10):
  ansMax = (arr[n-1][i][bitMask-1] + ansMax) % mod
print(ansMax)
