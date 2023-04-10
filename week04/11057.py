import sys

input = sys.stdin.readline

n = int(input().rstrip())
mom = 1
son = 10
for i in range(1, n):
    mom *= (1 + i)
    son *= (10 + i)

print((son // mom) % 10006)
