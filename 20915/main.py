import sys

N = int(sys.stdin.readline())

for i in range(N):
    t = sys.stdin.readline()
    t = t.replace('6', '9')

    li = list(t)
    li.sort(reverse=True)

    tmp = [li[0], li[1]]

    for c in li[2:]:
        if int(tmp[0] + c) * int(tmp[1]) > int(tmp[0]) * int(tmp[1] + c):
            tmp[0] += c
        else:
            tmp[1] += c

    #print(tmp[0], tmp[1])
    print(int(tmp[0]) * int(tmp[1]))