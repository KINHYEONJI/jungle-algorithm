import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
q = deque()
while True:
    info = int(input().strip())
    if info == -1:
        break
    elif info == 0:
        if len(q) != 0:
            q.popleft()

    else:
        if len(q) < N:
            q.append(info)

if len(q) == 0:
    print("empty")
else:
    print(*q)
