import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    sticker = [[0] + list(map(int, input().rstrip().split())) for _ in range(2)]
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]

    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]
    if n == 1:
        print(max(dp[0][1], dp[1][1]))
    else:

        for i in range(2, n + 1):
            dp[0][i] = sticker[0][i] + max(dp[1][i - 2], dp[1][i - 1])
            dp[1][i] = sticker[1][i] + max(dp[0][i - 2], dp[0][i - 1])

        print(max(dp[0][n], dp[1][n]))
