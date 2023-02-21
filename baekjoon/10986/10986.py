import sys


def solution(n, m, a):
    r_cnt = [0 for _ in range(m)]
    r_cnt[0] = 1

    result = 0
    psum = 0
    for i in range(n):
        psum = (psum + a[i]) % m
        result += r_cnt[psum]
        r_cnt[psum] += 1

    return result

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
a = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

print(solution(n, m, a))