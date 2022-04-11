import sys

def func(li, l):
    if len(li) > l:
        if li[-1] == 'A':
            func(li[:-1], l)

        if li[0] == 'B':
            func(li[1:][::-1], l)

    elif len(li) == l:
        if li == S:
            print(1)
            exit(0)




S = list(sys.stdin.readline()[:-1])
T = list(sys.stdin.readline()[:-1])

func(T, len(S))

print(0)