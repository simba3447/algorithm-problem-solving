import sys

def solution(tree, a, b):
    path_a = []
    path_b = []
    while True:
        path_a.append(a)
        if not tree.get(a):
            break
        a = tree[a][0]
    
    while True:
        path_b.append(b)
        if not tree.get(b):
            break
        b = tree[b][0]

    nca = path_a.pop()
    path_b.pop()

    while path_a and path_b:
        if path_a[-1] != path_b[-1]:
            break
        nca = path_a.pop()
        path_b.pop()
    
    return nca
            

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    tree = {}
    for i in range(1, n+1):
        tree[i] = []
    for _ in range(n - 1):
        a, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
        tree[b].append(a)
    a, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    print(solution(tree, a, b))
