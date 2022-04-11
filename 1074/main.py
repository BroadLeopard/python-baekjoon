import sys

def func(n, r, c, hap):
    if n == 0:
        print(hap)

    else:
        if 2**(n-1) <= r and 2**(n-1) <= c:#4번째
            hap += 2**(2*n - 2) * 3
            r -= 2**(n-1)
            c -= 2**(n-1)

        elif 2**(n-1) <= r and c <= 2**(n-1):#3번째
            hap += 2**(2*n - 2) * 2
            r -= 2**(n-1)

        elif 2**(n-1) >= r and 2**(n-1) <= c:#2번째
            hap += 2**(2*n - 2)
            c -= 2**(n-1)

        func(n-1, r, c, hap)



N, r, c = map(int, sys.stdin.readline().split())

func(N, r, c, 0)




