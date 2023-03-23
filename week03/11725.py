import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

answer = [0] * (n + 1)
visited = [False] * (n + 1)


# 재귀
# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             answer[i] = v
#             dfs(graph, i, visited)

# 스택₩
def dfs(graph, v, visited):
    stack = []
    visited[v] = True
    stack.append(v)

    while stack:
        x = stack.pop()
        for i in graph[x]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                answer[i] = x


dfs(graph, 1, visited)

for i in range(2, n + 1):
    print(answer[i])
