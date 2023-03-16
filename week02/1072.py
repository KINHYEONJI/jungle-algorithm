import sys

input = sys.stdin.readline

X, Y = map(int, input().strip().split())

start = 1
end = X
before_Z = Y * 100 // X

while start <= end:
    mid = (start + end) // 2

    after_Z = (Y + mid) * 100 / (X + mid)

    if after_Z <= before_Z:
        start = mid + 1

    else:
        end = mid - 1

if end + 1 > X:
    print(-1)
else:
    print(end + 1)
