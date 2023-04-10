# import sys
#
# input = sys.stdin.readline
#
# n = int(input().rstrip())
#
# matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
#
# dp = [[2 ** 31 for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     dp[i][i] = 0
#
# for i in range(1, n):
#     for j in range(0, n - i):
#         dp[j][j + i] = min(dp[j][j + i - 1] + matrix[j][0] * matrix[j + i - 1][1] * matrix[j + i][1],
#                            dp[j + 1][j + i] + matrix[j][0] * matrix[j + 1][0] * matrix[j + i][1])
#
# print(dp)
# print(dp[0][-1])

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(0, N - i):

        if i == 1:
            dp[j][j + i] = matrix[j][0] * matrix[j][1] * matrix[j + i][1]
            continue

        dp[j][j + i] = 2 ** 32
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i],
                               dp[j][k] + dp[k + 1][j + i] + matrix[j][0] * matrix[k][1] * matrix[j + i][1])

print(dp[0][N - 1])
