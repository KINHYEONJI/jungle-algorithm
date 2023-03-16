import sys

input = sys.stdin.readline

N, K = map(int, input().strip().split())

level_list = sorted(list(int(input().strip()) for _ in range(N)))

start = level_list[0]
end = start + K

while start <= end:
    mid = (start + end) // 2
    upgrade = 0

    for level in level_list:
        if level < mid:
            upgrade += (mid - level)

    if upgrade < K:
        start = mid + 1

    else:
        end = mid - 1

print(start)
