import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def normal(graph):
    count = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = deque()
                visited[i][j] = True
                q.append([i, j])
                count += 1

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if graph[nx][ny] == graph[x][y]:
                                q.append([nx, ny])
                                visited[nx][ny] = True

    return count


def unnormal(graph):
    count = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = deque()
                visited[i][j] = True
                q.append([i, j])
                count += 1

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if graph[x][y] == "R" and graph[nx][ny] == "G":
                                q.append([nx, ny])
                                visited[nx][ny] = True
                            elif graph[x][y] == "G" and graph[nx][ny] == "R":
                                q.append([nx, ny])
                                visited[nx][ny] = True
                            elif graph[nx][ny] == graph[x][y]:
                                q.append([nx, ny])
                                visited[nx][ny] = True

    return count


print(normal(graph), unnormal(graph))
