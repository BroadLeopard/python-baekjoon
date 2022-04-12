import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(N):
    for j in range(i + 1, N):
        if li[i] > li[j]:
            answer += 1

print(answer)
