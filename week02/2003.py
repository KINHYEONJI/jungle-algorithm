import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

numbers = list(map(int, input().strip().split()))

start, end = 0, 1
count = 0

while start <= end <= N:
    sum_ = sum(numbers[start: end])

    if sum_ == M:
        count += 1

    if sum_ >= M:
        start += 1
    else:
        end += 1

print(count)
