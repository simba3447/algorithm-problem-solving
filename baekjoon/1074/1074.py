import sys

def solution(n, r, c):
    if r == c == 0:
        return 0
    max_rc = max(r, c) 
    # print(max_rc)
    i = 1
    while (i * 2 <= max_rc):
        i *= 2
    
    visit = 0
    if r >= i:
        r -= i
        visit += (i ** 2) * 2
    if c >= i:
        c -= i
        visit += (i ** 2)
    
    return visit + solution(n, r, c)
    
n, r, c = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, r, c))