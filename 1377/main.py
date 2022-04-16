import sys

N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]

answer = 0

for i in range(N):
    li[i] = [li[i], i]#과거 좌표

li.sort()

for i in range(N):
    if li[i][1] - i > answer:#
        answer = li[i][1] - i

# print(li)

print(answer + 1)
