import sys
import math

def func(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)


Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, sys.stdin.readline().split())
dx, dy, dz = Bx - Ax, By - Ay, Bz - Az
left = 0.0
right = 1.0

while right - left > 1e-10:
    m1 = left + (right - left) / 3
    m2 = left + (right - left) * 2 / 3

    if func(Ax + m1 * dx, Ay + m1 * dy, Az + m1 * dz, Cx, Cy, Cz) > func(Ax + m2*dx, Ay + m2*dy, Az + m2 * dz, Cx, Cy, Cz):
        left = m1
    else:
        right = m2

ans = func(Ax + (m1 + m2)/2 * dx, Ay + (m1 + m2)/2 * dy, Az + (m1 + m2)/2 * dz, Cx, Cy, Cz)

print(f'{ans :.10f}')
