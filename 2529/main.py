import sys
import itertools

mi = 10000000000
ma = -10000000000

def func(num, digit):
    l = len(num)
    global k
    global lis
    if l == k + 1:
        global mi, ma
        mi = min(mi, int(num))
        ma = max(ma, int(num))
    else:
        for i in range(10 - l):
            if lis[l - 1] == '<' and num[-1] < digit[i]:
                func(num + digit[i], digit[:i] + digit[i+1:])
            elif lis[l - 1] == '>' and num[-1] > digit[i]:
                func(num + digit[i], digit[:i] + digit[i+1:])

k = int(sys.stdin.readline())
lis = list(sys.stdin.readline().split())
digit = ['0', '1', '2','3', '4', '5', '6', '7', '8', '9']


for i in range(10):
    func(digit[i], digit[:i] + digit[i+1:])

print(ma)
if len(str(mi)) == k:
    mi = '0' + str(mi)
print(mi)



# import sys
# import itertools
#
# mi = 10000000000
# ma = -10000000000
#
# k = int(sys.stdin.readline())
# lis = list(sys.stdin.readline().split())
# digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# li = list(itertools.permutations(digit, k + 1))
#
#
# for tLi in li:
#     flag = True
#     for i in range(k):
#         if lis[i] == '<' and  tLi[i] < tLi[i + 1]:
#             pass
#         elif lis[i] == '>' and tLi[i] > tLi[i+1]:
#             pass
#         else:
#             flag = False
#             break
#     if flag:
#         tmp = 0
#         for d in range(k + 1):
#             tmp += tLi[d] * 10**(k - d)
#
#         ma = max(ma, tmp)
#         mi = min(mi, tmp)
#
# ma = str(ma)
# mi = str(mi)
#
# if len(mi) == k:
#     mi = '0' + mi
#
# print(ma)
# print(mi)
#
#
#
#
#
