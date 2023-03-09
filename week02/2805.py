import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))
start, end = 0, max(trees)

while (start <= end):
    mid = (start + end) // 2

    wood_sum = 0

    for tree in trees:
        if tree > mid:
            wood_sum += (tree - mid)

    if wood_sum >= M:
        start = mid + 1

    else:
        end = mid - 1

print(end)
