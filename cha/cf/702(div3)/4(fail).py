import math

t = int(input())

def solve(arr, tree, left, right, treeIdx):
  if left >= right or treeIdx >= len(tree):
    return
  
  maxNum = 0
  maxIdx = -1
  
  for idx in range(left, right):
    el = arr[idx]
    if el > maxNum:
      maxIdx = idx
      maxNum = el
  tree[treeIdx] = maxNum
  solve(arr, tree, left, maxIdx, treeIdx*2)
  solve(arr, tree, maxIdx+1, right, treeIdx*2 +1)

for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  tree = [0] * (pow(2,n) + 1)
  solve(arr, tree, 0, len(arr), 1)
  res = []
  for aEl in arr:
    for idx, tEl in enumerate(tree):
      if aEl == tEl:
        res.append(int(math.log(idx,2)))
  for r in res:
    print(r, end=' ')
  print()