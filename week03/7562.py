import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
for _ in range(n):
    l = int(input().rstrip())
    now = list(map(int, input().rstrip().split()))
    want = list(map(int, input().rstrip().split()))
    graph = [[sys.maxsize for _ in range(l)] for _ in range(l)]

    q = deque()
    q.append(now)

    graph[now[0]][now[1]] = 0

    while q:
        x, y = q.popleft()

        if [x, y] == want:
            print(graph[want[0]][want[1]])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] > graph[x][y] + 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])


