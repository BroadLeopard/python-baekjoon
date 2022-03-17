import sys

N, S = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

if sum(li) < S:
    print(0)
else:
    start = 0
    end = 0
    answer = 100001

    sumA = li[0]

    while end < N:
        if sumA < S:
            end += 1

            if end == N:
                break
            sumA += li[end]
        else:
            answer = min(answer, end - start)
            sumA -= li[start]
            start += 1

    print(answer + 1)

