import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [[]]
for _ in range(N):
    graph.append([0] + list(map(int, input().rstrip())))

break_count = [[sys.maxsize for _ in range(N + 1)] for _ in range(N + 1)]
visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()


def dijkstra(x, y):
    q.append([x, y])
    break_count[x][y] = 0
    visited[x][y] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx < N + 1 and 0 < ny < N + 1:
                now_break_count = break_count[x][y]
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True

                if graph[nx][ny] == 0:
                    now_break_count += 1

                if now_break_count < break_count[nx][ny]:
                    break_count[nx][ny] = now_break_count
                    q.append([nx, ny])

            else:
                continue


dijkstra(1, 1)
print(break_count[-1][-1])
