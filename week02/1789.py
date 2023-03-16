import sys

input = sys.stdin.readline

N = int(input().strip())
start = 1
end = N

while start <= end:
    mid = (start + end) // 2

    sum_ = mid * (mid + 1) // 2

    if sum_ <= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
