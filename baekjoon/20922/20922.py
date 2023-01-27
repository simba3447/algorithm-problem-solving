import sys

def solution(n, k, a):
    i = j = 0

    answer = 0
    elements = [0 for _ in range(100001)]

    while (i < n and j < n):
        if elements[a[j]] == k:
            if answer < j - i:
                answer = j - i

            while elements[a[j]] == k:
                elements[a[i]] -= 1
                i += 1
        
        elements[a[j]] += 1
        j += 1

    if answer < j - i:
        answer = j - i
        
    return answer


n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
a = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, k, a))