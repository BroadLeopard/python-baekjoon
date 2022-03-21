import sys
import itertools

N = int(sys.stdin.readline())

li = [0 for _ in range(26)]


for _ in range(N):
    tmp = sys.stdin.readline()[:-1]

    l = len(tmp)

    for i in range(l):
        li[ord(tmp[i]) - 65] += 10**(l-1-i)

li.sort(reverse=True)

answer = 0

for i in range(10):
    answer += li[i]*(9-i)

print(answer)












# import sys
# import itertools
#
# N = int(sys.stdin.readline())
# se = set()
#
# li = []#들어온 글자
#
# for _ in range(N):
#     tmp = sys.stdin.readline()[:-1]
#     li.append(tmp)
#     se.update(list(tmp))
#
# lse = list(se)
# l = len(lse)
#
# num = [0,1,2,3,4,5,6,7,8,9]
# num = num[10 - l:10]
#
# perm = list(itertools.permutations(num))
#
# answer = -1
#
# for p in perm:
#     hap = 0
#
#     for s in li:
#         tmp = 0
#         for c in s:
#             tmp = tmp * 10 + p[ord(c) - 65]
#         hap += tmp
#
#     answer = max(answer, hap)
#
# print(answer)
