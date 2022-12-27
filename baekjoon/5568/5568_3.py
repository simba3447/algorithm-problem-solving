import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card_list = [sys.stdin.readline().rstrip() for _ in range(n)]

integer_set = set()

def count_integer(card_list, n, k, integer):
    if k == 0:
        integer_set.add(integer)
    
    for i in range(n):
        rest_card_list = card_list.copy()
        card = rest_card_list.pop(i)
        count_integer(rest_card_list, n-1, k-1, integer + card)

count_integer(card_list, n, k, '')

print(len(integer_set))
