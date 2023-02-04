import sys

n = int(sys.stdin.readline())

nodes = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n - 1)]

tree = {}
for i in range(n):
    tree[i + 1] = []

for node in nodes:
    tree[node[0]].append([node[1], node[2]])
    tree[node[1]].append([node[0], node[2]])

def dfs(tree, root):
    visited = [0 for _ in range(n)]
    stack = [root]

    while(stack):
        node = stack.pop()

        for item in tree[node]:
            if item[0] != root and visited[item[0] - 1] == 0:
                stack.append(item[0])
                visited[item[0] - 1] = visited[node - 1] + item[1]
                
    return visited

def solution(tree):
    visited = dfs(tree, 1)
    max_length_node = visited.index(max(visited)) + 1
    visited = dfs(tree, max_length_node)
    return max(visited)
    
print(solution(tree))