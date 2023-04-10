import sys

input = sys.stdin.readline

h = int(input().rstrip())

triangle = [list(map(int, input().rstrip().split())) for _ in range(h)]

for i in range(1, h):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

print(max(triangle[h - 1]))
