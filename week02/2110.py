import sys

input = sys.stdin.readline

N, C = map(int, input().strip().split())

houses = sorted(list(int(input().strip()) for _ in range(N)))

start = 0
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(1, N):
        if houses[i] >= start + (i * mid):
            count += 1


