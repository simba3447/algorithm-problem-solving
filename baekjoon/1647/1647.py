import sys

def find(a):
    if disjoint_set[a] == a:
        return a
    
    disjoint_set[a] = find(disjoint_set[a])
    return disjoint_set[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    
    if rank[root_a] > rank[root_b]:
        disjoint_set[root_b] = root_a
    else:
        disjoint_set[root_a] = root_b
        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def solution(edges):
    weights = []
    for a, b, c in edges:
        if find(a - 1) == find(b - 1):
            continue
        union(a - 1, b - 1)
        weights.append(c)
    sum_weight = sum(weights[:-1])

    return sum_weight

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
disjoint_set = [i for i in range(n)]
rank = [0 for _ in range(n)]

edges = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(m)]
edges.sort(key=lambda item: item[2])
print(solution(edges))