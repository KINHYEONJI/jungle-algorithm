import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())

Vlist = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


# def dfs(Vlist, start):
#     visited = [False] * (n + 1)
#     stack = [start]
#     visited[start] = True
#     while stack:
#         v = stack.pop()
#         print(v, end=' ')
#         for i in Vlist[v]:
#             if not visited[i]:
#                 stack.append(i)
#                 visited[i] = True


def dfs(Vlist, start):
    print(start, end=' ')
    visited[start] = True
    for end in Vlist[start]:
        if not visited[end]:
            dfs(Vlist, end)


def bfs(Vlist, start):
    visited = [False] * (n + 1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        print(q[0], end=' ')
        for i in Vlist[q[0]]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
        q.popleft()


for _ in range(m):
    s, e = map(int, input().rstrip().split())
    Vlist[s].append(e)
    Vlist[e].append(s)

for i in range(1, n + 1):
    Vlist[i].sort()

dfs(Vlist, v)
print()
bfs(Vlist, v)
