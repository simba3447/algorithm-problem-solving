import sys

def get_max_partial_match(s):
    pi = [0 for _ in range(len(s))]

    begin = 1
    matched = 0
    
    while begin + matched < len(s):
        if s[matched] == s[begin + matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        elif matched == 0:
            begin += 1
        else:
            begin += matched - pi[matched - 1]
            matched = pi[matched - 1]

    return max(pi)

def solution(s):
    result = 0
    for i in range(len(s)):
        substr = s[i:]
        result = max(get_max_partial_match(substr), result)
    return result
    
s = sys.stdin.readline().rstrip()
print(solution(s))