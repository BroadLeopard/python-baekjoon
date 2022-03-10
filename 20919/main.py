import sys

T = int(sys.stdin.readline())

for i in range(T):
    n, q = map(int, sys.stdin.readline().split())
    S = list(map(int, sys.stdin.readline().split()))

    answer = 0

    for j in range(q):
        li = list(map(int, sys.stdin.readline().split()))

        if li[0] == 1:
            answer = 40000000

            for s in S:
                answer = min(s ^ li[1], answer)
            print(answer)

        elif li[0] == 2:
            answer = 0

            for s in S:
                answer = max(s ^ li[1], answer)
            print(answer)

        elif li[0] == 3:
            S.append(li[1])
            print(len(set(S)))

        elif li[0] == 4:
            answer = min(S)
            print(answer)
            cnt = S.count(answer)

            for i in range(cnt):
                S.remove(answer)

        else:
            answer = max(S)
            print(answer)

            cnt = S.count(answer)

            for i in range(cnt):
                S.remove(answer)
