import sys


N = int(sys.stdin.readline())

li = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if li[i]:
        primes.append(i)
        for j in range(2*i, N + 1, i):
            li[j] = False

#print(primes)

start, end = 0, 1
length = len(primes)
answer = 0

while end <= length:
    tmp = sum(primes[start:end])

    if tmp < N:
        end += 1
    elif tmp > N:
        start += 1
    else:
        end += 1
        answer += 1

print(answer)



