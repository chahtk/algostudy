import sys

cube = [
    [['w','w','w'],['w','w','w'],['w','w','w']],
    [['y','y','y'],['y','y','y'],['y','y','y']],
    [['r','r','r'],['r','r','r'],['r','r','r']],
    [['o','o','o'],['o','o','o'],['o','o','o']],
    [['g','g','g'],['g','g','g'],['g','g','g']],
    [['b','b','b'],['b','b','b'],['b','b','b']]
]
# print(cube[1][1])

# n=int(sys.stdin.readline())

# for i in range(n):
#     m=int(sys.stdin.readline())
k=sys.stdin.readline().split()
print(k)
print(k[1].pop())