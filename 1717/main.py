import sys


def func(num):#최상단 부모를 알려주는 역할로 나중에 내려옴
    if li[num] == num:
        return num

    tmp = func(li[num])
    li[num] = tmp
    return tmp


n, m = map(int, sys.stdin.readline().split())

li = []

for i in range(n+2):
    li.append(i)

for _ in range(m):
    i, a, b = map(int, sys.stdin.readline().split())

    if i == 0: #합집합
        ap = func(a)
        bp = func(b)

        if ap != bp:
            li[bp] = ap
    else:#교집합
        if func(a) == func(b):
            print("YES")
        else:
            print("NO")




