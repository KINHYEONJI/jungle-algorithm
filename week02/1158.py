import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().strip().split())

q = deque(range(1, N + 1))
count = 1
answer = []
while len(q) > 0:
    if count % K == 0:
        answer.append(q.popleft())
    else:
        q.append(q.popleft())
    count += 1
print("<", end="")
print(", ".join(map(str, answer)), end="")
print(">")
