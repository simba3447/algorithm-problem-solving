import sys
from itertools import combinations

def solution(word):
    stack = []
    pairs = []
    for i in range(len(word)):
        if word[i] == '(':
            stack.append(i)
        elif word[i] == ')':
            pairs.append([stack.pop(), i])
        else:
            continue
    subsets = []
    for i in range(1, len(pairs)+1):
        s = list(combinations(pairs,i))
        for i in s:
            indexes = []
            for j in i:
                indexes.append(j[0])
                indexes.append(j[1])
            subsets.append(indexes)

    words = set()
    for subset in subsets:
        w = ''
        for i in range(len(word) - 1):
            if i not in subset:
                w += word[i]
        
        words.add(w)

    words = list(words)
    words.sort()
    for w in words:
        print(w)
        
        
word = sys.stdin.readline()
solution(word)