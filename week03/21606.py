import sys

input = sys.stdin.readline

N = int(input().rstrip())
status = [0] + list(map(int, str(input().rstrip())))

Vlist = [[] for _ in range(N + 1)]
count = 0
while True:
    try:
        s, e = map(int, input().rstrip().split())
        Vlist[s].append(e)
        Vlist[e].append(s)
    except:
        break


def dfs(index):
    global count
    for end in Vlist[index]:
        if status[end] != 1 and visited[end] == False:
            visited[end] = True
            dfs(end)
        if status[end] == 1 and visited[end] == False:
            count += 1


for i in range(1, N + 1):
    if status[i] == 1:
        visited = [False] * (N + 1)
        visited[i] = True
        dfs(i)

print(count)
