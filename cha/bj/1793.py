tile = [1] * 251
res = []

def init():
  tile[1] = 1
  tile[2] = 3
  for i in range(3, 251):
    tile[i] = tile[i-1] + 2*tile[i-2]
init()
while True:
  try:
    n = int(input())
    res.append(tile[n])
  except:
    break  
for r in res:
  print(r)