import sys

T = int(sys.stdin.readline())

for i in range(T):
    n, k = map(int, sys.stdin.readline().split())
    A = sys.stdin.readline()

    li = []
    before = 0

    topping = A.count('1')

    if topping % k:
        print(0)
    else:
        portion = topping // k

        for i in range(k):
            cnt = 0

            for j in range(before, n):
                if A[j] == '1':
                    cnt += 1

                    if cnt == portion:
                        li.append(A[before:j + 1])
                        before = j + 1
                        break


    print(li)




