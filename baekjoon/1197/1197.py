import sys

v, e = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
edges = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()]
         for _ in range(e)]
group = [i for i in range(v)]
height = [0 for _ in range(v)]

edges.sort(key=lambda x: x[2])


def find(v):
    if group[v] == v:
        return v
    group[v] = find(group[v])
    return group[v]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return

    if height[root_a] > height[root_b]:
        group[root_b] = root_a
    else:
        group[root_a] = root_b
        if height[root_a] == height[root_b]:
            height[root_b] += 1


result = 0
for a, b, c in edges:
    a -= 1
    b -= 1
    if find(a) == find(b):
        continue

    union(a, b)
    result += c

print(result)
