import sys

def func(li, l):
    if len(li) > l:
        li2 = list(li)
        if li2[-1] == 'A':
            func(li2[:-1], l)

        if li2[0] == 'B':
            li2.reverse()
            func(li2[:-1], l)

    elif len(li) == l:
        if li == S:
            print(1)
            exit(0)




S = list(sys.stdin.readline()[:-1])
T = list(sys.stdin.readline()[:-1])

func(T, len(S))

print(0)