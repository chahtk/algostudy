import copy

n = int(input())

div = 1000000000
arr = [[0]*10 for _ in range(n)]
res = 0

def search(layer, visit):
  global res
  
  if layer == n:
    if not False in visit:
      res += 1
  
  v = copy.deepcopy(visit)
  for i in range(10):
    if layer == 0 and i ==0:
      continue
    

search(0, [False] * 10)