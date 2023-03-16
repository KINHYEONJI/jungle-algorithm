import sys
from collections import deque

input = sys.stdin.readline

case = int(input().strip())

for i in range(case):
    n, m = map(int, input().strip().split())
    queue = deque(list(map(int, input().strip().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front:
            count += 1
            if m < 0:
                print(count)
                break

        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1
