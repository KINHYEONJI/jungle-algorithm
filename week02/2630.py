import sys

N = int(input().strip())
area = [list(map(int, input().strip().split())) for _ in range(N)]

blue_cnt, white_cnt = 0, 0


def recursive(x, y, N):
    global blue_cnt, white_cnt
    color = area[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != area[i][j]:
                recursive(x, y, N // 2)
                recursive(x, y + N // 2, N // 2)
                recursive(x + N // 2, y, N // 2)
                recursive(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1


recursive(0, 0, N)
print(white_cnt)
print(blue_cnt)
