import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().strip().split())
q = deque(range(1, N + 1))

answer = []

while q:
    for i in range(K - 1):
        q.append(q.popleft())
    answer.append(q.popleft())

print("<" + ", ".join(map(str, answer)) + ">")
