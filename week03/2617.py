import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

ans = 0

for i in range(1, N + 1):
    left_cnt = 0
    right_cnt = 0
    for j in range(1, N + 1):
        if i == j:
            continue
        elif arr[i][j] == 1:
            right_cnt += 1
        elif arr[j][i] == 1:
            left_cnt += 1
    if right_cnt > N // 2 or left_cnt > N // 2:
        ans += 1

print(ans)

