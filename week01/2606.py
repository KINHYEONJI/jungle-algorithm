import sys

input = sys.stdin.readline

N, M = (int(input().strip()) for _ in range(2))

connect_list = [list(map(int, input().strip().split())) for _ in range(M)]

virus_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    virus_list[connect_list[i][0]].append(connect_list[i][1])
    virus_list[connect_list[i][1]].append(connect_list[i][0])
print(virus_list)
count = 0


def dfs(index):
    global count
    if virus_list[index] == '':
        return
    visited[index] = True
    for i in range(len(virus_list[index])):
        if not visited[virus_list[index][i]]:
            count += 1
            dfs(virus_list[index][i])


dfs(1)

print(count)
