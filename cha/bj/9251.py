strA = input()
strB = input()

table = [[0]*(len(strB)+1) for _ in range(len(strA)+1)]

ansMax = 0
for indexA, a in enumerate(strA):
  for indexB, b in enumerate(strB):
    tableIndexA = indexA + 1
    tableindexB = indexB + 1
    prev = table[tableIndexA-1][tableindexB-1]
    if a == b:
      table[tableIndexA][tableindexB] = prev + 1
    else:
      table[tableIndexA][tableindexB] = max(table[tableIndexA-1][tableindexB], table[tableIndexA][tableindexB-1])
    ansMax = max(table[tableIndexA][tableindexB], ansMax)

print(ansMax)
    
