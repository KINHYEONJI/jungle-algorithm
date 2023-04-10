import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

coins = [int(input().rstrip()) for _ in range(n)]
coins.reverse()
count = 0
for coin in coins:
    count += k // coin
    k %= coin

print(count)
