import sys

input = sys.stdin.readline

n = int(input().rstrip())
weights = list(int(input().rstrip()) for _ in range(n))

weights.sort()
max_ = 0

for i in range(n):
    if max_ < weights[i] * (n - i):
        max_ = weights[i] * (n - i)

print(max_)
