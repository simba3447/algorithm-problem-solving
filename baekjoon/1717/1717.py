import sys

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]
    
for _ in range(m):
    op, a, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    if op == 0:
        union(a, b)
    elif op == 1:
        if find(a) == find(b): print("YES")
        else: print("NO")
