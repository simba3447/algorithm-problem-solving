import sys

def solution(n, k, a):
    psum = 0
    pdict = {0: 1}
    
    cnt = 0
    for i in range(n):
        psum += a[i]
        if pdict.get(psum - k):
            cnt += pdict[psum - k]
        if not pdict.get(psum):
            pdict[psum] = 0
        pdict[psum] += 1
            
    return cnt

n, k = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
a = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
print(solution(n, k, a))