import sys


class dice:
    def __init__(self):
        self.area = [[0 for _ in range(3)] for _ in range(4)]

    def printArea(self):
        for i in range(4):
            print(self.area[i])

    def rotate(self, dir):
        if dir == 1:
            tmp = self.area[3][1]
            self.area[3][1] = self.area[1][2]
            self.area[1][2] = self.area[1][1]
            self.area[1][1] = self.area[1][0]
            self.area[1][0] = tmp

        elif dir == 2:
            tmp = self.area[3][1]
            self.area[3][1] = self.area[1][0]
            self.area[1][0] = self.area[1][1]
            self.area[1][1] = self.area[1][2]
            self.area[1][2] = tmp
            pass
        elif dir == 3:
            tmp = self.area[0][1]
            self.area[0][1] = self.area[1][1]
            self.area[1][1] = self.area[2][1]
            self.area[2][1] = self.area[3][1]
            self.area[3][1] = tmp
        elif dir == 4:
            tmp = self.area[3][1]
            self.area[3][1] = self.area[2][1]
            self.area[2][1] = self.area[1][1]
            self.area[1][1] = self.area[0][1]
            self.area[0][1] = tmp

    def get_up(self):
        return self.area[1][1]

    def get_down(self):
        return self.area[3][1]

    def set_down(self, num):
        self.area[3][1] = num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    di = dice()

    N, M, x, y, K = map(int, sys.stdin.readline().split())
    arr = []
    order = []

    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    order = list(map(int, sys.stdin.readline().split()))

    for cmd in order:
        if 0 <= x + dx[cmd] < N and 0 <= y + dy[cmd] < M:
            x += dx[cmd]
            y += dy[cmd]

            di.rotate(cmd)

            if arr[x][y] == 0:
                arr[x][y] = di.get_down()
            else:
                di.set_down(arr[x][y])
                arr[x][y] = 0

            # di.printArea()

            print(di.get_up())
