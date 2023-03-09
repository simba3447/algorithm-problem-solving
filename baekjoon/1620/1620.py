import sys

n, m = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
pokemons = [sys.stdin.readline().rstrip() for _ in range(n)]
pokemon_dict = {}
for i in range(len(pokemons)):
    pokemon_dict[pokemons[i]] = i + 1

for _ in range(m):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(pokemons[int(question) - 1])
    else:
        print(pokemon_dict[question])