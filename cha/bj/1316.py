n = int(input())
ans = 0
for _ in range(n):
  bit = [0] * 26
  string = input()
  prev = ''
  for s in string:
    if prev != s:
      bit[ord(s)-97] += 1
      prev = s
  if not max(bit) >= 2:
    ans += 1
print(ans)