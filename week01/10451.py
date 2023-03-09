import sys

input = sys.stdin.readline

T = int(input())
count = 0


def dfs(index, num_list):
    global count

    visited[index] = True
    temp.append(index)

    if num_list[index] in temp:
        count += 1
        return

    dfs(num_list[index], num_list)


for _ in range(T):
    N = int(input())
    num_list = [0] + list(map(int, input().strip().split()))
    visited = [False] * (N + 1)
    temp = []

    for i in range(1, N + 1):
        if visited[i] == False:
            dfs(i, num_list)

            temp = []
    print(count)
    count = 0
