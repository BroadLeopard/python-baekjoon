import sys

s, t = map(int, sys.stdin.readline().split())

if s == t:
    print(0)
    exit(0)
else:
    que = [[s, '']]
    flag = True

    while que:
        val, op = que.pop(0)


        if val == t:
            print(op)
            exit(0)
        elif val < t:
            if val != 1:
                que.append([val * val, op + '*'])

            que.append([val + val, op + '+'])

        if flag:
            flag = False
            que.append([1, op + '/'])

print(-1)
