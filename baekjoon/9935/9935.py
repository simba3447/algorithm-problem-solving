import sys


def solution(str, substr):
    stack = []
    buffer = []
    for char in str:
        stack.append(char)
        for sub_char in reversed(substr):
            if len(stack) > 0 and stack[-1] == sub_char:
                buffer.append(stack.pop())
            else:
                for _ in range(len(buffer)):
                    stack.append(buffer.pop())
                break
        buffer = []

    if len(stack) == 0:
        result = 'FRULA'
    else:
        result = ''.join(stack)
    return result


str = sys.stdin.readline().rstrip()
substr = sys.stdin.readline().rstrip()
print(solution(str, substr))
