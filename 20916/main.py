import sys

T = int(sys.stdin.readline())

l = [202021, 20202021, 202002021, 202012021, 202022021, 202032021, 202042021, 202052021, 202062021, 202072021, 202082021, 202092021]

for i in range(T):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    length = len(li)

    answer = 0

    for j in range(length):
        for k in range(j+1, length):
            if (li[j] + li[k]) in l:
                answer += 1

    print(answer)
