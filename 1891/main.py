import sys

d, num = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())
answer = ''

num = str(num)
ox, oy = 0, 0
nx, ny = 0, 0

for i in range(d):
    if num[i] == '1':
        ox += 2**(d - 1 - i)
        oy += 2**(d - 1 - i)
    if num[i] == '2':
        oy += 2**(d - 1 - i)
    if num[i] == '4':
        ox += 2**(d - 1 - i)

# print(ox, oy)


nx = ox + x
ny = oy + y

for i in range(d):
    if nx >= 2**(d - 1 - i) and ny >= 2**(d - 1 - i):
        answer += '1'
        nx -= 2**(d - 1 - i)
        ny -= 2**(d - 1 - i)
    elif nx >= 2**(d - 1 - i):
        answer += '4'
        nx -= 2**(d - 1 - i)
    elif ny >= 2**(d - 1 - i):
        answer += '2'
        ny -= 2**(d - 1 - i)
    else:
        answer += '3'

if nx == 0 and ny == 0:
    print(answer)
else:
    print(-1)