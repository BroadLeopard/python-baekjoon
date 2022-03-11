import sys
import itertools

T = int(sys.stdin.readline())

for _ in range(T):
    li = []#대문자 개수랑, 정렬시켜서 넣을 리스트

    n, k = map(int, sys.stdin.readline().split())

    li2 = list(sys.stdin.readline().split())

    answer = 0

    for i in range(n):
        cnt = [0 for _ in range(26)]
        tmp = 0

        for c in li2[i]:
            if c <= 'Z':
                tmp += 1

            cnt[ord(c.lower()) - ord('a')] += 1

        li.append([tmp, cnt])

    nC2 = list(itertools.combinations(li, 2))

    for a, b in nC2:
        if a == b:
            answer += 1

    #print(nC2)

    print(answer)
