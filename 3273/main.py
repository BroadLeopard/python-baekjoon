import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

li.sort()

answer = 0
start = 0
end = len(li) - 1

while start < end:
    if li[start] + li[end] > x:
        end -= 1
    elif li[start] + li[end] < x:
        start += 1
    else:
        answer += 1
        end -= 1
        start += 1

print(answer)