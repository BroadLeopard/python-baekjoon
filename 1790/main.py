import sys


def func(n):#특정 수까지 길이를 구하는 함수
    l = 0
    for i in range(12):
        if 10 ** (i + 1) <= n:
            l += (i + 1) * 9 * 10 ** i
        else:
            l += (n - 10 ** i + 1) * (i + 1)
            break

    return l


N, K = map(int, sys.stdin.readline().split())
tmp = 0
start = 1
end = N
tmp = 0

if func(N) < K:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2

        if func(mid) < K:
            start = mid + 1
            tmp = start
        else:
            end = mid - 1
            tmp = mid

print(str(mid)[   ])