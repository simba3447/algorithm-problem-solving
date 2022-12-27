import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

card_list = []
for i in range(n):
    card_list.append(sys.stdin.readline().rstrip())

def count_integer(card_list, k):
    integer_set = set()
    def count_integer_rec(card_list, k, integer):
        if k == 0:
            integer_set.add(integer)

        for i in range(len(card_list)):
            card = card_list[i]
            rest_card_list = card_list[:i] + card_list[i+1:]
            count_integer_rec(rest_card_list, k-1, integer + card)

    count_integer_rec(card_list, k, '')

    return len(integer_set)

print(count_integer(card_list, k))