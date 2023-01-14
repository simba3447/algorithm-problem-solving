import sys

dp = [[-1] * 300] * 100000

def solution(n, array):
    def path(x, sum):
        if x == n:
            return sum + array[x]
        return max([path(x + 1, sum + array[x]), path(x + 2, sum + array[x])])
    
    return 


n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]

print(solution(n, array))
