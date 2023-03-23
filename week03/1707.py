import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input().rstrip())


def dfs(i):
    global result
    for x in Vlist[i]:
        if visited[x] == -1:
            if visited[i] == 1:
                visited[x] = 2
            else:
                visited[x] = 1
            dfs(x)
        else:
            if visited[x] == visited[i]:
                result = False
                return


for i in range(N):
    v, e = map(int, input().rstrip().split())
    Vlist = [[] for _ in range(v + 1)]
    visited = [-1] * (v + 1)
    result = True
    for _ in range(e):
        x, y = map(int, input().rstrip().split())
        Vlist[x].append(y)
        Vlist[y].append(x)

    for i in range(1, v + 1):
        if visited[i] == -1:
            visited[i] = 1
            dfs(i)
            if result == False:
                break

    if result:
        print("YES")
    else:
        print("NO")
