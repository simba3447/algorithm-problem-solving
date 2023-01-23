import sys

def solution(a, b):
    answer = 1
    while a != 1 and b != 1:
        exist = False
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                a = a // i
                b = b // i
                answer *= i
                exist = True
                break
        if not exist:
            answer = answer * a * b
            break
    return answer

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
    print(solution(a, b))
