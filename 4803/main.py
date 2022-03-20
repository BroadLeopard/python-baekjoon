import sys

case = 0

while True:
    m, n = map(int, sys.stdin.readline().split())
    case += 1
    tree = 0

    if m == 0 and n == 0:
        break










    if tree == 0:
        print(f"Case {case}: No trees.")
    elif tree == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {tree} trees.")