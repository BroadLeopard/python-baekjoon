import sys

A, B, C, X, Y = map(int, sys.stdin.readline().split())

ans = A * X + B * Y

if X > Y:
    ans = min(ans, 2 * C * X)
    # print(2 * C * X)
    ans = min(ans, A * (X - Y) + C * 2 * Y)
    # print(A * (X - Y) + C * 2 * Y)
else:
    ans = min(ans, 2 * C * Y)
    # print(2 * C * Y)
    ans = min(ans, 2 * C * X + B * (Y - X))
    # print(2 * C * X + B * (Y - X))

print(ans)

