import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())
apples = [list(map(int, input().strip().split())) for _ in range(K)]
L = int(input().strip())
moves = [list(input().strip().split()) for _ in range(L)]

snake_hq = deque([[1, 1]])


def is_move(y, x, N, snake_hq):
    if 0 > x or x > N or 0 > y or y > N:
        return False
    if [y, x] in snake_hq:
        return False
    return True


count = 0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1], ]
direction_idx = 1
temp_time = 0

for move in moves:
    time, direction = move

    for _ in range(int(time) - temp_time):
        y = snake_hq[-1][0] + directions[direction_idx][0]
        x = snake_hq[-1][1] + directions[direction_idx][1]

        count += 1
        if is_move(y, x, N, snake_hq):
            snake_hq.append([y, x])
            if [y, x] not in apples:
                snake_hq.popleft()
        else:
            print(count)
            sys.exit()
    temp_time = int(time)
    if direction == "D":
        direction_idx = (direction_idx + 1) % 4
    elif direction == "L":
        direction_idx = (4 + (direction_idx - 1)) % 4

if direction_idx == 0:
    print(count + snake_hq[-1][0] - 1)
elif direction_idx == 1:
    print(count + (N - snake_hq[-1][1]) - 1)
elif direction_idx == 2:
    print(count + snake_hq[-1][1] - 1)
elif direction_idx == 3:
    print(count + (N - snake_hq[-1][0]) - 1)
