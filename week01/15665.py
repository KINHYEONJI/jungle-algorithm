import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
temp= []

def dfs(depth, index) :
    if(depth == M):
        print(*temp)
        return

    before = 0
    for i in range(0, N) :
        if (before != num_list[i]):
            temp.append(num_list[i])

            before = num_list[i]
            dfs(depth+1, i+1)

            temp.pop()

dfs(0, 0)