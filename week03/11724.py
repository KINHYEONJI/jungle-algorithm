import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
temp = []

for i in range(m):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)


def dfs(index):
    if visited[index] == True:
        return
    visited[index] = True

    for i in range(len(graph[index])):
        dfs(graph[index][i])
    return


count = 0

for i in range(1, n + 1):
    if (visited[i] == False):
        dfs(i)
        count += 1

print(graph)
print(count)
