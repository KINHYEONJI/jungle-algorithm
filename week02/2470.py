import sys

input = sys.stdin.readline

N = int(input().strip())

nums = sorted(list(map(int, input().strip().split())))

start = 0
end = N - 1

answer = sys.maxsize
temp = []

while start < end:
    left = nums[start]
    right = nums[end]

    now = left + right

    if abs(now) < answer:
        answer = abs(now)
        temp = [left, right]

    if now < 0:
        start += 1

    else:
        end -= 1

print(temp[0], temp[1])
