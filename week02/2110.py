import sys

input = sys.stdin.readline

N, C = map(int, input().strip().split())

houses = sorted(list(int(input().strip()) for _ in range(N)))

start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    count = 1
    before_house = houses[0]
    for i in range(1, N):
        if houses[i] >= before_house + mid:
            count += 1
            before_house = houses[i]

    if count >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)
