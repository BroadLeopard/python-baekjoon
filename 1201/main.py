import sys

R, C = map(int, sys.stdin.readline().split())

li = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

answer = ''

if R % 2 == 0:
    if C % 2:#C는 홀수
        for j in range(C):
            if j % 2:
                for i in range(R-1):
                    answer += 'U'
            else:
                for i in range(R-1):
                    answer += 'D'

            if j != C - 1:
                answer += 'R'

    else:#둘 다 짝수
        if li[R-1][C-2] > li[R-2][C-1]:
            for i in range(R-2):
                if i % 2:
                    for j in range(C - 1):
                        answer += 'L'
                else:
                    for j in range(C - 1):
                        answer += 'R'

                if i != R - 1:
                    answer += 'D'

            for j in range(C):
                if j % 2:
                    answer += 'U'
                else:
                    answer += 'D'

                if j != C - 1:
                    answer += 'R'

        else:
            for j in range(C - 2):
                if j % 2:
                    for i in range(R - 1):
                        answer += 'U'
                else:
                    for i in range(R - 1):
                        answer += 'D'

                if j != C - 1:
                    answer += 'R'

            for i in range(R):
                if i % 2:
                    answer += 'L'
                else:
                    answer += 'R'

                if i != R - 1:
                    answer += 'D'


        answer = answer[:-1]
else:#R 홀수
    for i in range(R):
        if i % 2:
            for j in range(C - 1):
                answer += 'L'
        else:
            for j in range(C-1):
                answer += 'R'

        if i != R - 1:
            answer += 'D'

print(answer)
