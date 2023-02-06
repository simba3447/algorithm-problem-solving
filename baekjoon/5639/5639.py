import sys


def solution(preorder: list[int]) -> None:
    postorder = []
    stack = [(0, len(preorder) - 1)]
    while stack:
        s, e = stack.pop()
        if s > e:
            continue
        root = preorder[s]
        postorder.append(root)
        valid = False
        for i in range(s + 1, e + 1):
            if preorder[i] > root:
                valid = True
                stack.append((s + 1, i - 1))
                stack.append((i, e))
                break
        if not valid:
            stack.append((s + 1, e))
    
    for _ in range(len(postorder)):
        print(postorder.pop())

preorder = []
while True:
    node = sys.stdin.readline().rstrip()
    if not node:
        break
    preorder.append(int(node))

solution(preorder)