import sys

def func(num, S):
    if len(S) == 1:
        return 1

    sum = 0

    for i in range(1, len(S)):
        if int(num, 16) > int(S[:i], 16):
            return 0
        elif int(S[:i], 16) > int(S[i], 16):
            return 0
        else:
            sum += func(S[:i], S[i:]) + 1

    return sum

T = int(sys.stdin.readline())

for _ in range(T):
    S = sys.stdin.readline()

    print(func("0", S[:-1]))

