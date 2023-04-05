import sys

if __name__ == '__main__':
    N, L = map(int, sys.stdin.readline().split())
    answer = 0

    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    def cal(x, y):
        v = arr[x][y]

        for




    for i in range(N):#가로줄 검사
        for j in range(1, N):

            if arr[i][j - 1] != arr[i][j]:#크기가 다른 경우
                if abs(arr[i][j] - arr[i][j - 1]) > 1:#크기 차이 1 넘은 경우
                    break
                elif abs(arr[i][j] - arr[i][j - 1]) == 1:#크기 차이 1인 경우
                    if j < L or cal(i, j):
                        break











            if j == N - 1:
                answer += 1







        
        
        
        

    print(answer)
    