import sys, copy

sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

remember_area = [list(map(int, input().strip().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_floor = max([val for row in remember_area for val in row])


def dfs(height, x, y):
    if x < 0 or x >= N or y < 0 or y >= N or area[x][y] <= height:
        return

    if area[x][y] > height:
        area[x][y] = 0
        for i in range(4):
            dfs(height, x + dx[i], y + dy[i])
        return True


safe_area = []

for i in range(max_floor):
    area = copy.deepcopy(remember_area)
    count = 0
    for y in range(N):
        for x in range(N):
            if dfs(i, x, y) == True:
                count += 1
    safe_area.append(count)

print(max(safe_area))
