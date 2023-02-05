import sys

def find(s, e):
    global preorder
    global inorder
    if s > e:
        return
    root = preorder.pop()
    index = inorder.index(root)
    find(s, index - 1)
    find(index + 1, e)
    print(root, end=' ')
    
def solution(n, preorder, inorder):
    find(0,len(preorder) - 1)
    print()

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preorder = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    preorder.reverse()
    inorder = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    solution(n, preorder, inorder)