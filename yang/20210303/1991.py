# # import sys

# # pre=[]


# class Node:
#     def __init__(self,item):
#         self.item = item
#         self.left = None

#         self.right = None


# class ByTree():

#     def __init__(self):
#         self.root=None


#     def preorder(self,n):

#         if n!= None:

#             pre.append(n.item)
#             if n.left:
#                 self.preorder(n.left)
#             if n.right:
#                 self.preorder(n.right)

#     def inorder(self,n):
#         if n!= None:

#             if n.left:
#                 self.preorder(n.left)
#             pre.append(n.item)
#             if n.right:
#                 self.preorder(n.right)


#     def postorder(self,n):
#         if n!= None:

#             if n.left:
#                 self.preorder(n.left)
#             if n.right:
#                 self.preorder(n.right)
#             pre.append(n.item)


# tree=ByTree()
# # n1=Node('a')
# # n2=Node(2)
# # n3=Node(3)    
# # n4=Node(4)
# # n5=Node(5)

# # tree.root=n1

# # n1.left=n2
# # n1.right=n3
# # n2.left=n4
# # n2.right=n5

# #n=int(input())

# # for i in range(n):
# #     m=input().split()



# # tree.preorder(tree.root)

# n=int(input())

# m=[]
# for i in range(n):
#     [root,r,l]=input().split()
#     m.append([root,r,l])

# for i in range(n):
#     print(m[i])

# print(m)


# for i in range(n):
#     globals()['n{}'.format(i)]=Node(m[i][0])
#     print('n{}'.format(i))




