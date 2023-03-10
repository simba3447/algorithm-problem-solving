import sys


def solution(n, meetings):
    meetings.sort()
    
    prev_e = 0
    cnt = 0
    for i in range(len(meetings)):
        s, e = meetings[i]
        
        if i > 0:
            if s >= prev_e:
                prev_e = e
                cnt += 1
            elif e <= prev_e:
                prev_e = e   
        else:
            prev_e = e
            cnt += 1

    return cnt


n = int(sys.stdin.readline())
meetings = [[int(i) for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(n)]
print(solution(n, meetings))