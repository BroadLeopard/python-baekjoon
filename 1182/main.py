import sys
import itertools

N, S = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(1, N + 1):
    tmp = list(itertools.combinations(li, i))


    for k in tmp:
        if sum(k) == S:
            answer += 1

print(answer)

