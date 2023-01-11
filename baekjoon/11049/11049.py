import sys

def solution(s, e): # s: Index of First Element, e: Index of Last Element
    if e == s:
        return 0

    if dp[s][e] != -1:
        return dp[s][e]

    answer = 1e9
    for i in range(s+1, e+1):
        ax, _ = array[s]
        bx, _ = array[i]
        _, by = array[e]
        op = ax * bx * by
        sum = op + solution(s, i-1) + solution(i, e)
        if sum < answer:
            answer = sum

    dp[s][e] = answer
    
    return answer


n = int(sys.stdin.readline())
array = [[int(i) for i in sys.stdin.readline().rstrip().split()] for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

print(solution(0, n-1))