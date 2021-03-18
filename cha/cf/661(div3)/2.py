t = int(input())
res = []
for _ in range(t):
  n = int(input())
  candy = list(map(int, input().split()))
  orange = list(map(int, input().split()))

  count = 0
  minCandy = min(candy)
  minOrg = min(orange)

  for i in range(n):
    diffCandy = candy[i] - minCandy
    diffOrg = orange[i] - minOrg

    # both
    minOfThem = min(diffCandy, diffOrg)
    count += minOfThem
    diffCandy -= minOfThem
    diffOrg -= minOfThem

    # candy
    count += diffCandy
    # orange
    count += diffOrg
  res.append(count)

for r in res:
  print(r)