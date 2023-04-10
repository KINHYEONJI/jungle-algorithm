import sys

X = sys.stdin.readline().rstrip()
Y = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(X) + 1)] for _ in range(len(Y) + 1)]

for j in range(1, len(Y) + 1):
    for i in range(1, len(X) + 1):
        if X[i - 1] == Y[j - 1]:
            dp[j][i] = dp[j - 1][i - 1] + 1
        else:
            dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

print(dp[-1][-1])
