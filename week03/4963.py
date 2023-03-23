import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


def bfs(graph, w, h):
    q = deque()
    count = 2
    for i in range(h):
        for j in range(w):

            if graph[i][j] == 1:
                q.append([i, j])
                graph[i][j] = count

                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < h and 0 <= ny < w:
                            if graph[nx][ny] == 1:
                                graph[nx][ny] = graph[x][y]
                                q.append([nx, ny])
                count += 1


while True:
    w, h = map(int, input().rstrip().split())

    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().rstrip().split())))
    bfs(graph, w, h)
    max = -sys.maxsize
    for i in range(h):
        for j in range(w):
            if max < graph[i][j]:
                max = graph[i][j]

    if max == 0:
        print(0)
    else:
        print(max - 1)
