import sys

answer = ''


def func1(sr, sc, dr, dc): # 왼쪽에서 오른쪽으로
    global answer
    for i in range(sr, dr):
        if i % 2:
            answer += 'L' * (dc - sc - 1)
        else:
            answer += 'R' * (dc - sc - 1)

        answer += 'D'


def func2(sr, sc, dr, dc): #위에서 아래로
    global answer
    for j in range(sc, dc):
        if j % 2:
            answer += 'U' * (dr -sr - 1)
        else:
            answer += 'D' * (dr - sr - 1)

        answer += 'R'


R, C = map(int, sys.stdin.readline().split())

rc = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]


if R % 2 == 0:
    if C % 2:#C는 홀수
        func2(0, 0, R, C)

    else:#둘 다 짝수
        minBlack = 10000000
        r, c = 0, 0

        for i in range(R):
            for j in range(C):
                if (i + j) % 2 and minBlack > rc[i][j]:
                    minBlack = rc[i][j]
                    r, c = i, j

        if r % 2:
            func1(0, 0, r, C)

        else:
            func1()

else:#R 홀수
    func1(0, 0, R, C)

print(answer[:-1])
