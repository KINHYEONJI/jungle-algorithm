import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

answer = []
q = deque()
distance = [-1] * (n + 1)


def bfs(start):
    q.append(start)
    distance[start] = 0

    while q:
        s = q.popleft()
        for e in graph[s]:
            if distance[e] < 0:
                q.append(e)
                distance[e] = distance[s] + 1


bfs(x)

for i in range(1, n + 1):
    if distance[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    print(*answer, sep="\n")
