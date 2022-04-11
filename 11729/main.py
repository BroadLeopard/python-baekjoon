import sys

def func(n, x, y):
    if n == 0:
        return
    func(n - 1, x, 6 - x - y)
    print(x, y)
    func(n - 1, 6 - x - y, y)


N = int(sys.stdin.readline())

print(2**N - 1)
func(N, 1, 3)