n, m, k = map(int, input().split())
arr = [0] * n
tree = [0] * (n*4)
query = [[] for _ in range(m+k)]

for i in range(n):
  arr[i] = int(input())
for i in range(m+k):
  query[i] = list(map(int, input().split()))

def initTree(node, start, end):
  if start == end:
    tree[node] = arr[start]
    return tree[node]
  mid = (start+end)//2
  tree[node] = initTree(node*2, start, mid) + initTree(node*2+1, mid+1, end)
  return tree[node]
initTree(1, 0, n-1)

def searchTree(node, start, end, left, right):
  if end < left or right < start:
    return 0
  if left <= start and end <= right:
    return tree[node]
  mid = (start+end)//2
  return searchTree(node*2, start, mid, left, right) + searchTree(node*2+1, mid+1, end, left, right)

def updateTree(node, start, end, index, diff):
  if not start <= index <= end:
    return
  tree[node] += diff
  if start == end:
    return
  mid = (start+end) // 2
  updateTree(node*2, start, mid, index, diff)
  updateTree(node*2+1, mid+1, end, index, diff)

for q in query:
  mode = q[0] # 1: update, 2: search sum
  if mode == 1:
    updateTree(1, 0, n-1, q[1]-1, q[2] - arr[q[1]-1])
    arr[q[1]-1] = q[2]
  if mode == 2:
    print(searchTree(1, 0, n-1, q[1]-1, q[2]-1))

'''
2 1 3
5
2
2 1 2
1 1 2
2 1 1
2 1 2

5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5

3 1 3
-2
-5
4
2 1 3
2 2 3
1 1 2
2 1 2

5 2 2
1
2
3
4
5
1 3 6
2 1 5
1 3 3
2 1 5
'''