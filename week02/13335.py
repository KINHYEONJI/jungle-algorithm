import sys
from collections import deque

input = sys.stdin.readline

n, w, l = map(int, input().strip().split())
trucks = list(map(int, input().strip().split()))
q = deque(0 for _ in range(w))
time = 0
i = 0

while q:
    if i == n:
        break

    q.popleft()
    time += 1

    if sum(q) + trucks[i] <= l:
        q.append(trucks[i])
        i += 1
    else:
        q.append(0)

print(time + w)
