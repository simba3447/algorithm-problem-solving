import sys

def solution(fomula):
    priority = {
        '*': 1,
        '/': 1,
        '+': 2,
        '-': 2,
        '(': 3,
    }
    stack = []

    for char in fomula:
        if char == '(':
            stack.append(char)
        elif char == '*' or char == '/':
            while len(stack) > 0 and priority[stack[-1]] <= 1:
                print(stack.pop(), end='')
            stack.append(char)
        elif char == '+' or char == '-':
            while len(stack) > 0 and priority[stack[-1]] <= 2:
                print(stack.pop(), end='')
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        else:
            print(char, end='')

    for _ in range(len(stack)):
        print(stack.pop(), end='')

s = sys.stdin.readline().rstrip()
solution(s)
