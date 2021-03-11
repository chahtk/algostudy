'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

cards.sort()

def lowerBound(key):
  # 같거나 가장 가까운 큰 수
  start, end = 0, len(cards)
  
  while start < end:
    mid = (start+end) // 2
    if cards[mid] >= key:
      end = mid
    else:
      start = mid + 1
  
  return start

# print(cards)
for query in queries:
  print(lowerBound(query+1) - lowerBound(query), end = ' ')
