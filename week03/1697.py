import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

arr = [sys.maxsize] * (100001)
arr[n] = 0

q = deque()

q.append(n)

dx = [-1, 1]

while q:
    x = q.popleft()
    for i in range(2):
        nx = x + dx[i]
        if 0 <= nx < 100001 and arr[nx] > arr[x] + 1:
            arr[nx] = arr[x] + 1
            q.append(nx)

    if 0 <= 2 * x < 100001 and arr[2 * x] > arr[x] + 1:
        arr[2 * x] = arr[x] + 1
        q.append(2 * x)

    if x == k:
        print(arr[k])
