import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

T = int(input().strip())


def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < N):
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dfs(nx, ny)


for _ in range(T):
    M, N, K = map(int, input().strip().split())
    graph = [[0] * M for _ in range(N)]
    bug = 0

    for i in range(K):
        x, y = map(int, input().strip().split())
        graph[y][x] = 1

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                dfs(x, y)
                bug += 1

    print(bug)
