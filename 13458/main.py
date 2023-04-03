import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B, C = map(int, sys.stdin.readline().split())
    answer = N

    for i, a in enumerate(A):
        A[i] = max(0, A[i] - B)

        answer += (A[i] + C - 1) // C

    print(answer)
