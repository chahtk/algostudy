# input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = [[] for _ in range(m)]
for i in range(m):
  qry = list(map(int, input().split()))
  query[i] = qry

# init tree
tree = [-1] * (n*4)
def initTree(node, start, end):
  if start == end:
    tree[node] = arr[start]
    return tree[node]
  mid = (start+end)//2
  tree[node] = initTree(node*2, start, mid) + initTree(node*2+1, mid+1, end)
  return tree[node]

initTree(1, 0, n-1)

# search tree
def searchTree(node, start, end, qS, qE):
  if qS > end or qE < start:
    return 0
  if qS <= start and end <= qE:
    return tree[node]
  mid = (start+end)//2
  return searchTree(node*2, start, mid, qS, qE) + searchTree(node*2+1, mid+1, end, qS, qE)

for qS, qE in query:
  print(searchTree(1, 0, n-1, qS-1, qE-1))

'''
5 3
5 4 3 2 1
1 3
2 4
5 5
------
 9   6
 9     3
5 4 3 2 1
'''