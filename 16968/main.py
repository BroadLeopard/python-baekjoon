import sys


def func(down):
    l = len(down)
    if l == num:
        flag = True
        for i in range(1, l):
            if down[i-1] == down[i]:
                flag = False
                break

        if flag:
            global ans
            ans += 1

    else:

        if f[l] == 'c':
            for i in range(97, 123):
                func(down + chr(i))

        else:
            for i in range(10):
                func(down + str(i))




f = sys.stdin.readline()[:-1]
ans = 0
num = len(f)

func('')

print(ans)