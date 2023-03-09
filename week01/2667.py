import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global count

    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True


count = 0

for y in range(N):
    for x in range(N):
        if dfs(x, y) == True:
            answer.append(count)
            count = 0

print(len(answer), *sorted(answer), sep="\n")
