import sys

candidate = []
pm = [-1, 0, 1]
ans = 1000000000


N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

if N < 3:
    print(0)
    exit(0)

#앞에 있는 숫자 3개만 조절하면 된다.

for i in range(3):
    for j in range(3):
        for k in range(3):
            if B[0] + pm[i] + B[2] + pm[k] == 2*(B[1] + pm[j]):
                candidate.append([B[0] + pm[i], B[1] + pm[j], B[2] + pm[k]])


#print(candidate)


for c in candidate:
    d = c[1] - c[0] # 등차
    tmp = 0
    flag = True

    v = c[0]

    if B[0] != c[0]:
        tmp += 1

    for i in range(len(B)):
        v += d
        if abs(v - B[i]) == 1:
            tmp += 1
        elif v == B[i]:
            pass
        else:
            flag = False
            break

    if flag:
        ans = min(ans, tmp)

if ans == 1000000000:
    print(-1)
else:
    print(ans)