import sys

input = sys.stdin.readline

M, N, L = map(int, input().strip().split())
M_list = sorted(list(map(int, input().strip().split())))
animals = [list(map(int, input().strip().split())) for i in range(N)]
count = 0


def binary_search(M_list, x):
    start = 0
    end = len(M_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if M_list[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return end


for animal in animals:
    x, y = animal
    near_m = binary_search(M_list, x)

    dist = abs(x - M_list[near_m]) + y
    dist_right = abs(x - M_list[near_m + 1]) + y if near_m < M - 1 else sys.maxsize

    dist = min(dist, dist_right)

    if dist <= L:
        count += 1

print(count)
