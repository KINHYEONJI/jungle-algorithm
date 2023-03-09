import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
temp = []


def dfs(index):
    if visited[index] == True:
        return

    visited[index] = True
    for i in range(len(graph[index])):
        dfs(graph[index][i])
    return


count = 0

for i in range(1, N + 1):
    if (visited[i] == False):
        dfs(i)
        count += 1

print(count)
