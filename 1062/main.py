import sys
import itertools

N, K = map(int, sys.stdin.readline().split())

li = []
alpha = set()
answer = 0
left = 0

plus = 0

if K > 4:
    left = K - 5



for _ in range(N):
    tmp = set(sys.stdin.readline()[:-1])
    tmp.remove('a')
    tmp.remove('n')
    tmp.remove('t')
    tmp.remove('i')
    tmp.remove('c')




