import sys

N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

start, end = 0, N - 1
a, b = 0, 0
sum = 2000000000
answer1, answer2 = 0, 0

li.sort()

if li[0] > 0:
    print(li[0], li[1])
elif li[-1] < 0:
    print(li[-2], li[-1])
else:
    while start < end:
        if abs(sum) > abs(li[start] + li[end]):
            sum = li[start] + li[end]
            a = li[start]
            b = li[end]

        if abs(li[start]) < abs(li[end]):
            end -= 1
        elif abs(li[start]) > abs(li[end]):
            start += 1
        else:
            break

    print(a, b)





