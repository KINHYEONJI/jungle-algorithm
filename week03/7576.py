import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
tomatos = [[]] + [[0] + list(map(int, input().rstrip().split())) for _ in range(n)]
q = deque()

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if tomatos[i][j] == 1:
            q.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
temp = [1]
answer = 0

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 < nx < n + 1 and 0 < ny < m + 1:
            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                temp.append(tomatos[x][y] + 1)
                q.append([nx, ny])

answer = temp[-1] - 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if tomatos[i][j] == -0:
            answer = -1

print(answer)
