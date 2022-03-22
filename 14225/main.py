import sys
import itertools

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

tmp = []

for i in range(1, len(li) + 1):
    combi = itertools.combinations(li, i)

    for c in combi:
        tmp.append(sum(c))


tmp = list(set(tmp))

tmp.sort()

i = 1

for e in tmp:
    if e == i:
        i += 1
    else:
        break

print(i)

