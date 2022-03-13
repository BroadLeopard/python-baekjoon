import sys


def func(num, S):
    length = len(S)

    if length == 1:
        return 0

    sum = 0

    for i in range(1, length):
        if int(num, 16) <= int(S[:i], 16) <= int(S[i:], 16):  #앞의 숫자보다 큼
            #print(S[:i], S[i:])
            sum += func(S[:i], S[i:]) + 1

    return sum

T = int(sys.stdin.readline())

for _ in range(T):
    S = sys.stdin.readline()

    print(func("0", S[:-1]) + 1)

