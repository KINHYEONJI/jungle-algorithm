import sys

input = sys.stdin.readline


def maxSize():
    max_size = 0
    stack = []

    for i in range(N):
        min_point = i
        while stack and stack[-1][0] >= rect[i]:
            h, min_point = stack.pop()
            tmp_size = h * (i - min_point)
            max_size = max(max_size, tmp_size)
        stack.append([rect[i], min_point])
        
    for h, point in stack:
        max_size = max(max_size, (N - point) * h)

    return max_size


while True:
    N, *rect = map(int, input().strip().split())
    if N == 0:
        break
    print(maxSize())
