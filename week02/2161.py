import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

q = deque(list(range(1, N + 1)))
answer = []
while q:
    answer.append(q.popleft())
    if len(q) == 0:
        break
    q.append(q.popleft())

print(*answer)
