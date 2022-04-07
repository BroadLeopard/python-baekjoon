import sys

S = list(sys.stdin.readline()[:-1])
T = list(sys.stdin.readline()[:-1])

for _ in range(len(T) - len(S)):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()

if S == T:
    print(1)
else:
    print(0)


