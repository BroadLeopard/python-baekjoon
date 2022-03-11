import sys

def func(num):
    num = str(num)

    if len(num) < 6:
        return False

    if num[:4] == "2020" and num[-4:] == "2021":
        return True

    return False


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())

    liA = list(map(int, sys.stdin.readline().split()))
    setA = set(liA)
    liA2 = list(setA)

    length = len(liA2)

    answer = 0

    for i in range(length):
        for j in range(i+1, length):
            if func(liA2[i] + liA2[j]):
                answer += liA.count(liA[i]) * liA.count(liA[j])

    print(answer)



