import sys

def func(num):
    if li[num][0] == li[num][1]:
        return li[num][0]
    else:
        return func(li[num][0])



n, m = map(int, sys.stdin.readline().split())

li = [0] * n + 1

for i in range(n+1):
    li[i] = [i, i]

for _ in range(m):
    i, a, b = map(int, sys.stdin.readline().split())

    if i == 0:
        ap = func(a)
        bp = func(b)
        x = min(ap, bp)
        li[a] = x
        li[b] = x

    else:


        if li[a][0] == li[b][0]:
            print("YES")
        else:
            print("NO")




