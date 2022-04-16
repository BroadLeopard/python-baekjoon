import sys
import math

x, y, c = map(float, sys.stdin.readline().split())
left, right = 0, min(x, y)
ans = 0
# - A * c + A * B = c * B

for _ in range(10000):
    mid = (left + right) / 2

    h1 = math.sqrt(x**2 - mid**2)
    h2 = math.sqrt(y**2 - mid**2)

    if (h1 + h2) * c - h1 * h2 < 0:# k를 키워야 한다.
        left = mid
    else:
        right = mid

print(f'{left : .3f}')






