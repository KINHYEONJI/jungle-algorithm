import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    coins = map(int, input().rstrip().split())
    money = int(input().rstrip())
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, money + 1):
            dp[i] += dp[i - coin]
    print(dp[money])
