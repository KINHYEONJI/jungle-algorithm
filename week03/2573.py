import sys
from collections import deque

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ice = [list(map(int, input().rstrip().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
melting_count = [[0 for _ in range(M)] for _ in range(N)]


def reduce():
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if ice[i][j] - melting_count[i][j] < 0:
                ice[i][j] = 0
            else:
                ice[i][j] -= melting_count[i][j]


def fine_melting_count():
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if ice[i][j] != 0:
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]

                    if ice[x][y] == 0:
                        melting_count[i][j] += 1


def check():
    count = 0
    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if ice[i][j] != 0 and not visited[i][j]:
                count += 1
                q.append([i, j])
                visited[i][j] = True

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if ice[nx][ny] > 0 and not visited[nx][ny]:
                        q.append([nx, ny])
                        visited[nx][ny] = True

            if count > 1:
                return count

    return count


i = 0

while True:
    i += 1
    melting_count = [[0 for _ in range(M)] for _ in range(N)]
    fine_melting_count()
    reduce()
    count = check()

    if count > 1:
        print(i)
        break

    elif count == 0:
        print(0)
        break
