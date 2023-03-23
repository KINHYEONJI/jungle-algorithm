import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
map_ = [[]]

for _ in range(r):
    map_.append([0] + list(input().rstrip()))

q = deque()

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if map_[i][j] == "S":
            q.append(["S", i, j])
            map_[i][j] = 0

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if map_[i][j] == '*':
            q.append(["*", i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


def dijkstra():
    global answer
    while q:
        s, x, y = q.popleft()
        if s == "*":

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 < nx < r + 1 and 0 < ny < c + 1:
                    if map_[nx][ny] != "D" and map_[nx][ny] != "X" and map_[nx][ny] != "*":
                        map_[nx][ny] = "*"
                        deque.append(q, ["*", nx, ny])

        elif s == "S":

            if not str(map_[x][y]).isnumeric():
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 < nx < r + 1 and 0 < ny < c + 1:
                    if map_[nx][ny] == "D":
                        answer = map_[x][y] + 1
                        return

                    if map_[nx][ny] == ".":
                        map_[nx][ny] = map_[x][y] + 1
                        deque.append(q, ["S", nx, ny])

            map_[x][y] = "."


dijkstra()

if answer == 0:
    print("KAKTUS")
else:
    print(answer)
