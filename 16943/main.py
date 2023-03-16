import sys

def func(li, li2):
    if len(li) == len(A):
        global ans

        if li[0] != '0' and int("".join(li)) < B:
            ans = max(ans, int("".join(li)))
    else:
        for i in range(len(li2)):
            func(li + [li2[i]], li2[:i] + li2[i + 1:])



A, B = sys.stdin.readline()[:-1].split()
B = int(B)
ans = -1

func([], list(A))

print(ans)