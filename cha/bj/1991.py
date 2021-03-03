import sys

class Node:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None
  def getData(self):
    return self.data


class Tree:
  def __init__(self):
    self.root = None
    self.set = set() # 'A', 'B'
    self.nodes = [] # A의 노드, B의 노드

  def setRoot(self, root):
    self.root = root

  def getNode(self, data):
    for node in self.nodes:
      if node.getData() == data:
        return node

  def makeTree(self, p, left, right):
    pNode = None
    if p in self.set: # value 'B'
      pNode = self.getNode(p)
    else:
      self.set.add(p)
      pNode = Node(p)
      self.nodes.append(pNode)
    if not left == '.':
      if left in self.set:
        lNode = self.getNode(left)
        pNode.leftChild = lNode
      else:
        self.set.add(left)
        lNode = Node(left)
        self.nodes.append(lNode)
        pNode.leftChild = lNode
    if not right == '.':
      if right in self.set:
        rNode = self.getNode(right)
        pNode.rightChild = rNode
      else:
        self.set.add(right)
        rNode = Node(right)
        self.nodes.append(rNode)
        pNode.rightChild = rNode

  def search1(self, node):
    print(node.getData(), end='')
    if node.leftChild:
      self.search1(node.leftChild)
    if node.rightChild:
      self.search1(node.rightChild)

  def search2(self, node):
    if node.leftChild:
      self.search2(node.leftChild)
    print(node.getData(), end='')
    if node.rightChild:
      self.search2(node.rightChild)

  def search3(self, node):
    if node.leftChild:
      self.search3(node.leftChild)
    if node.rightChild:
      self.search3(node.rightChild)
    print(node.getData(), end='')

n = int(sys.stdin.readline())

tree = Tree() # tree

for _ in range(n):
  [p, left, right] = sys.stdin.readline().split()
  tree.makeTree(p, left, right)

tree.search1(tree.getNode('A'))
print()
tree.search2(tree.getNode('A'))
print()
tree.search3(tree.getNode('A'))

# 121220 KB
# celar time: 112ms