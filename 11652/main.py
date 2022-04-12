import sys

N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
li.sort()

preLen = 0
preVal = 0
curLen = 1
curVal = li[0]


for i in range(1, len(li)):
    if li[i-1] != li[i]:
        if preLen < curLen:
            preLen = curLen
            preVal = curVal

        curLen = 1
        curVal = li[i]

    else:
        curLen += 1


if preLen >= curLen:
    print(preVal)
else:
    print(curVal)


