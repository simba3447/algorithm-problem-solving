import sys

v = int(sys.stdin.readline())
tree = {i + 1:[] for i in range(v)}
for _ in range(v):
    edges = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    s = edges[0]
    for i in range(len(edges) // 2 - 1):
        tree[s].append((edges[i * 2 + 1], edges[i * 2 + 2]))

def dfs(tree, v, start):
    stack = [start]
    distances = [0 for _ in range(v)]

    while stack:
        node = stack.pop()
        for item in tree[node]:
            if item[0] != start and distances[item[0] - 1] == 0:
                distances[item[0] - 1] = distances[node - 1] + item[1]
                stack.append(item[0])

    return distances

distances = dfs(tree, v, 1)
i = distances.index(max(distances)) + 1
distances = dfs(tree, v, i)
print(max(distances))