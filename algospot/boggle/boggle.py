# Brute Force Approach

import sys

c = int(sys.stdin.readline())
boards = [[sys.stdin.readline().rstrip() for _ in range(5)] for _ in range(c)]
n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

def find(board, word):
    def find_rec(board, word, current_x, current_y):
        if len(word) == 0:
            return True
        
        first_letter = word[0]
        result = False
        for i in range(3):
            for j in range(3):
                moved_x = current_x + 1 - i
                moved_y = current_y + 1 - j
                if not (i == 1 and j == 1) and 0 <= moved_x < 5 and 0 <= moved_y < 5 and board[moved_y][moved_x] == first_letter:
                    if find_rec(board, word[1:], moved_x, moved_y):
                        result = True
        return result

    for i in range(5):
        for j in range(5):
            if find_rec(board, word, i, j):
                return True
    return False

for word in words:
    if any(find(board, word) for board in boards):
        result = 'YES'
    else:
        result = 'NO'
    print('{} {}'.format(word, result))
