import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().rstrip().split())
graph = [[]]
q = deque([])

for i in range(1, h + 1):
    graph.append([])
    graph[i].append([])
    for j in range(1, n + 1):
        graph[i].append([0] + list(map(int, input().rstrip().split())))
        for k in range(1, m + 1):
            if graph[i][j][k] == 1:
                deque.append(q, [i, j, k])

# 후, 전, 좌, 우, 상, 하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

res = []


#
def dijkstra():
    while q:
        z, x, y = q.popleft()
        for i in range(6):

            nz = z + dx[i]
            nx = x + dy[i]
            ny = y + dz[i]

            if 0 < nx < n + 1 and 0 < ny < m + 1 and 0 < nz < h + 1:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    res.append(graph[nz][nx][ny])
                    deque.append(q, [nz, nx, ny])


dijkstra()

answer = 0

if len(res) == 0:
    answer = 0
else:
    answer = res[-1] - 1

for i in range(1, h + 1):
    for j in range(1, n + 1):
        for k in range(1, m + 1):
            if graph[i][j][k] == 0:
                answer = -1
                break

print(answer)
