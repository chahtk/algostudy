import math

n = int(input())
ans = {}

for i in range(n):
  string = input()
  length = len(string)
  total = 0
  for index, s in enumerate(string):
    num = ord(s) - 96
    total += num * int(math.pow(26, length-index-1))
  ans[total] = string

for key in sorted(ans.keys()):
  print(ans[key])
