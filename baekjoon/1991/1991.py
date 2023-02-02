import sys

n = int(sys.stdin.readline())

nodes = [sys.stdin.readline().rstrip().rsplit() for _ in range(n)]

def preorder(n):
    node = nodes[n]
    print(node[0], end='')
    if node[1] != '.':
        for i in range(len(nodes)):
            if nodes[i][0] == node[1]:
                preorder(i)
                break
    if node[2] != '.':
        for i in range(len(nodes)):
            if nodes[i][0] == node[2]:
                preorder(i)
                break

def inorder(n):
    node = nodes[n]
    if node[1] != '.':
        for i in range(len(nodes)):
            if nodes[i][0] == node[1]:
                inorder(i)
                break
    print(node[0], end='')
    if node[2] != '.':
        for i in range(len(nodes)):
            if nodes[i][0] == node[2]:
                inorder(i)
                break

def postorder(n):
    node = nodes[n]
    if node[1] != '.':
        for i in range(len(nodes)):
            if nodes[i][0] == node[1]:
                postorder(i)
                break
    if node[2] != '.':
        for i in range(len(nodes)):
            if nodes[i][0] == node[2]:
                postorder(i)
                break
    print(node[0], end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)