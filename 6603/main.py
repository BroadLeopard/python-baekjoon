import sys
import itertools

def func(left, li, num):
    if num == 6:
        print(*left)
    else:
        for i in range(len(li)):
            func(left + [li[i]], li[i+1:], num + 1)


while True:
    li = list(map(int, sys.stdin.readline().split()))

    if li[0] == 0:
        break

    func([], li[1:], 0)


    print()

