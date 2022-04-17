import sys


N, k = map(int, sys.stdin.readline().split())
num = 0# 어떤 숫자인지 가르킨다
tmp = 0#임시 길이
r = 0

for i in range(1, 10):
    if tmp + 9*i*10**(i-1) <= k:
        tmp += 9*i*10**(i-1)
        num += 9*10**(i-1)
    else:
        r = (k - tmp) % i
        if r: #r이 0이 아니면 내가 원하는 숫자는 q + 1
            num += (k - tmp) // i + 1
        else: #r이 0이면 그 숫자의 마지막 자리에 있다는 뜻
            num += (k - tmp) // i
        break

if N < num:
    print(-1)
else:
    print(str(num)[r - 1])



