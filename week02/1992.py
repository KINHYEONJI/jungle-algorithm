import sys

input = sys.stdin.readline

N = int(input().strip())
black_white_area = [list(map(int, input().strip())) for _ in range(N)]

stack = []


def recursive(x, y, N):
    black_white = black_white_area[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if black_white != black_white_area[i][j]:
                stack.append("(")
                recursive(x, y, N // 2)
                recursive(x, y + N // 2, N // 2)
                recursive(x + N // 2, y, N // 2)
                recursive(x + N // 2, y + N // 2, N // 2)
                stack.append(")")
                return

    if black_white == 0:
        stack.append("0")
    else:
        stack.append("1")


recursive(0, 0, N)

print("".join(stack))
