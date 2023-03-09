import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(set(map(int, input().split()))))
temp= []


def dfs(depth, index):
    if(depth == M) :
        print(*temp)
        return

    for i in range(index, len(num_list)) :
        temp.append(num_list[i])
        dfs(depth+1, i)
        temp.pop()

dfs(0, 0)
