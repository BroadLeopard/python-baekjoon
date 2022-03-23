import sys

ma = -1000000000
mi = 1000000000

def func(i, num, li):
    if i == N:
        global ma
        global mi
        ma = max(ma, num)
        mi = min(mi, num)
    else:
        for t in range(4):
            if li[t] > 0:
                if t == 0:
                    li[t] -= 1
                    func(i+1, num + A[i], li)
                    li[t] += 1
                elif t == 1:
                    li[t] -= 1
                    func(i+1, num - A[i], li)
                    li[t] += 1
                elif t == 2:
                    li[t] -= 1
                    func(i+1, num * A[i], li)
                    li[t] += 1
                else:
                    li[t] -= 1
                    if num < 0 and A[i] > 0:
                        func(i + 1, -(-num // A[i]), li)
                    else:
                        func(i+1, num // A[i], li)
                    li[t] += 1



N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
opera = list(map(int, sys.stdin.readline().split()))

num = A[0]

func(1, num, opera)


print(ma)
print(mi)


