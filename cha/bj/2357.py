n, m = map(int, input().split())
arr = [0] * n
query = [[] for _ in range(m)]
for i in range(n):
  arr[i] = int(input())
for i in range(m):
  query[i] = list(map(int, input().split()))

tree = [0] * (n*4)
def initTree(node, start, end):
  if start == end:
    tree[node] = [arr[start]] * 2
    return tree[node]
  mid = (start+end)//2
  leftChild, rightChild = initTree(node*2, start, mid), initTree(node*2+1, mid+1, end)
  tree[node] = [max(leftChild[0],rightChild[0]), min(leftChild[1],rightChild[1])]
  return tree[node]
initTree(1, 0, n-1)

def searchTree(node, start, end, left, right):
  if right < start or end < left:
    return [0, 1e9]
  if left <= start and end <= right:
    return tree[node]
  mid = (start+end)//2
  leftChild, rightChild = searchTree(node*2, start, mid, left, right), searchTree(node*2+1, mid+1, end, left, right)
  return [max(leftChild[0], rightChild[0]), min(leftChild[1], rightChild[1])]

for q in query:
  maxVal, minVal = searchTree(1, 0, n-1, q[0]-1, q[1]-1)
  print(minVal, maxVal)