import sys


def find(n, i, prev):
    answer = 0
    for j in range(n):
        valid = True
        for k in range(i):
            index_diff = k - i
            if prev[k] == j or abs(prev[k] - j) == abs(index_diff):
                valid = False
                break
        if not valid:
            continue

        if i == n-1:
            return 1

        curr = prev.copy()
        curr[i] = j
        answer += find(n, i+1, curr)
    return answer

    
def solution(n):
    prev = [-1 for _ in range(n)]
    return find(n, 0, prev)

n = int(sys.stdin.readline())
array = [-1 for _ in range(n)]

print(solution(n))
