import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

maze = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = maze[0][0]

        elif i == 0:
            dp[i][j] = dp[i][j - 1] + maze[i][j]

        elif j == 0:
            dp[i][j] = dp[i - 1][j] + maze[i][j]

        else:
            dp[i][j] = maze[i][j] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[-1][-1])
