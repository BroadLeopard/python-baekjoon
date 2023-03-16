import sys

def func(li, num):
    if num == N:
        global ans
        if L <= sum(li) <= R and X <= li[-1] - li[0]:
            ans += 1
    else:
        func(li + [A[num]], num + 1)
        func(li, num + 1)

N, L, R, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
ans = 0

func([], 0)

print(ans)