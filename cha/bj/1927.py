import heapq
import sys

minHeap = []
res = []

n = int(input())

for _ in range(n):
  x = int(sys.stdin.readline())
  if x != 0:
    heapq.heappush(minHeap, x)
  else:
    res.append(heapq.heappop(minHeap) if len(minHeap) > 0 else 0)

for item in res:
  print(item)