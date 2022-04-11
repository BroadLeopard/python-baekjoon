import sys

li = []

def func(i, p):
    if p:
        num = i.index(p[-1])#p의 마지막 부분을 기준으로 삼는다.
        li.append(p[-1])

        func(i[:num], p[:num])#인오더의 앞부분, 포스트 오더 앞부분
        func(i[num + 1:], p[num: -1])#인오더의 뒷부분, 포스트 오더 뒷부분


n = int(sys.stdin.readline())

inOrder = list(map(int, sys.stdin.readline()[:-1].split()))
postOrder = list(map(int, sys.stdin.readline()[:-1].split()))


func(inOrder, postOrder)

print(*li)

