import sys

def solution(n, adj):
    result = [[i for i in col] for col in adj]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != k and j != k:
                    if adj[i][j] > adj[i][k] + adj[k][j]:
                        return -1
                    if adj[i][j] == adj[i][k] + adj[k][j]:
                        result[i][j] = 0

    optimal_sum = sum(map(sum, result)) // 2
    
    return optimal_sum

n = int(sys.stdin.readline())
adj = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]

print(solution(n, adj))