import sys

N = int(sys.stdin.readline())

for i in range(N):
    t = sys.stdin.readline()
    zero = t.count('0')
    t = t.replace('6', '9')
    t = t.replace('0', '')

    li = list(t)
    li.sort(reverse =True)

    tmp = ['', '']
    a = 1
    b = 0

    for c in li:
        if c == '\n':
            continue

        if a < 2:
            tmp[0] += c
            a += 1

            if a == 2 and b == 2:
                b = 0

        elif b < 2:
            tmp[1] += c
            b += 1

            if b == 2 and a == 2:
                a = 0

    for i in range(zero):
        tmp[1] += '0'

    print(tmp[0], tmp[1])
    print(int(tmp[0]) * int(tmp[1]))