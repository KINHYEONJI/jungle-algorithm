import sys

input = sys.stdin.readline

n = int(input().rstrip())
v = int(input().rstrip())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(v):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

stack = []


def virus(start):
    if visited[start] == True:
        return

    visited[start] = True

    for i in range(len(graph[start])):
        if visited[graph[start][i]] == False:
            stack.append(graph[start][i])
            virus(graph[start][i])
    return


virus(1)
print(len(stack))
