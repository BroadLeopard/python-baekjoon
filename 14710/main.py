th1, th2 = map(int, input().split())

if th1 % 30 * 12 == th2:
    print("O")
else:
    print("X")