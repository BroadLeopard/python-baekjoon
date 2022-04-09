import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
answer = 0

A.sort(reverse=True)
B.sort()

for a, b in zip(A, B):
    answer += a*b

print(answer)