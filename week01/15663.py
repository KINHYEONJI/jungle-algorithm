import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
temp= []
visited = [False]*N

def dfs(depth) :
    if(depth == M) :
        print(*temp)
        return
    before = 0
    for i in range(0, N):
        if not visited[i] and (before != num_list[i]) :
            temp.append(num_list[i])
            visited[i] = True
            before = num_list[i]
            dfs(depth+1)
            visited[i] = False
            temp.pop()

dfs(0)

