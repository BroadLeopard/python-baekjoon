
s = set()

N = int(input())

for i in range(N + 1):# 1, 5, 10, 50 에서 합쳐서는 20
    for j in range(N - i + 1):
        for k in range(N - i - j + 1):
            s.add(i*1 + j*5 + k*10 + (N - i - j - k) * 50)

print(len(s))
