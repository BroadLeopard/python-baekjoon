import sys

C, P = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
blocks = [[[0,0,0,0], [0]], [[0, 0]], [[1,1,0], [0, 1]], [[0,1,1], [1, 0]], [[0,0,0], [1, 0], [0, 1, 0], [0, 1]],
         [[0,0,0], [0,0], [1,0,0], [0,2]], [[0,0,0], [2, 0], [0,0,1], [0,0]]]
ans = 0

block = blocks[P - 1]

for shape in block:
    l = len(shape)
    for i in range(C - l + 1):
        tmp = li[i] + shape[0]  # 높이
        flag = True
        for j in range(1, l):
            if li[i + j] + shape[j] != tmp:
                flag = False
                break

        if flag:
            ans += 1


print(ans)






