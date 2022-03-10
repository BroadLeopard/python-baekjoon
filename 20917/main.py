import sys

T = int(sys.stdin.readline())

for i in range(T):
    s, n = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    li.sort()

    start = 0
    end = li[-1]
    answer = 0

    while start <= end:
        cnt = 1
        tmp = li[0]
        mid = end - start

        for i in range(len(li) - 1):
            if tmp + mid <= li[i+1]:
                cnt += 1
                tmp = li[i+1]

        if cnt < n:  #거리가 긴 경우 줄인다.
            end = mid - 1
        else: # 거리가 짧은 경우 늘린다.
            start = mid + 1
            answer = mid


    print(answer)