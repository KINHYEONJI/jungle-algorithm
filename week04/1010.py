import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, m = map(int, input().rstrip().split())
    son, mom = 1, 1
    if m - n < m // 2:
        for i in range(m, n, -1):
            son *= i
        for i in range(m - n, 0, -1):
            mom *= i

    else:
        for i in range(m, m - n, -1):
            son *= i
        for i in range(n, 0, -1):
            mom *= i

    print(son // mom)
