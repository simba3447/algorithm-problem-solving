import sys

dictionary = {}
cnt = 0
while True:
    name = sys.stdin.readline().rstrip()
    if name == '':
        break
    if dictionary.get(name) is not None:
        dictionary[name] += 1
    else:
        dictionary[name] = 1
    
    cnt += 1

keys = list(dictionary.keys())
keys.sort()
for item in keys:
    print("{} {:.4f}".format(item, dictionary[item] / cnt * 100))