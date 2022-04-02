import sys

N = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline()[:-1]))
li2 = list(map(int, sys.stdin.readline()[:-1]))
li3 = list(li2)

flag2 = False
flag3 = False

ans2 = 1
ans3 = 0

# 누름

li2[0] = 1 - li2[0]
li2[1] = 1 - li2[1]

for i in range(N - 2):
    if li2[i] != li[i]:
        li2[i] = 1 - li2[i]
        li2[i + 1] = 1 - li2[i + 1]
        li2[i + 2] = 1 - li2[i + 2]
        ans2 += 1

if li2[N - 2] != li[N - 2]:
    li2[N - 2] = 1 - li2[N - 2]
    li2[N - 1] = 1 - li2[N - 1]
    ans2 += 1

if li2[N-1] == li[N-1]:
    flag2 = True


# 안 누름

for i in range(N - 2):
    if li3[i] != li[i]:
        li3[i] = 1 - li3[i]
        li3[i + 1] = 1 - li3[i + 1]
        li3[i + 2] = 1 - li3[i + 2]
        ans3 += 1

if li3[N - 2] != li[N-2]:
    li3[N - 2] = 1 - li3[N - 2]
    li3[N - 1] = 1 - li3[N - 1]
    ans3 += 1

if li3[N-1] == li[N-1]:
    flag3 = True

if flag2 and flag3:
    print(min(ans2, ans3))
elif flag2:
    print(ans2)
elif flag3:
    print(ans3)
else:
    print(-1)
