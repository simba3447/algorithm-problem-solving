import sys

def solution(string, commads):
    i = [char for char in string]
    j = []

    for cmd in commands:
        if cmd[0] == "P":
            i.append(cmd[1])
        elif cmd[0] == "L":
            if len(i) > 0:
                j.append(i.pop())
        elif cmd[0] == "D":
            if len(j) > 0:
                i.append(j.pop())
        elif cmd[0] == "B":
            if len(i) > 0:
                i.pop()
    
    answer = ""
    for char in i:
        answer += char
    for char in reversed(j):
        answer += char
    return answer
        
string = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline())
commands = [[i for i in sys.stdin.readline().rstrip().rsplit()] for _ in range(m)]

print(solution(string, commands))