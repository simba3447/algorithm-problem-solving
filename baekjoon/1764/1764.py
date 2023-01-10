import sys

n, m = (int(i) for i in sys.stdin.readline().split())

nl = set()
for _ in range(n):
    nl.add(sys.stdin.readline().rstrip())
nml = []

for _ in range(m):
    s = sys.stdin.readline().rstrip()
    if s in nl:
        nml.append(s)

nml.sort()

print(len(nml))
for i in nml:
    print(i)
