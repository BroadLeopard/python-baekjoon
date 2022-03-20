import sys

answer = 1



N, C = map(int,sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

func(C, li)

print(answer)



