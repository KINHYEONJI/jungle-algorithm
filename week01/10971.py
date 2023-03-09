# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# N = int(input())
# W = [list(map(int, input().strip().split())) for _ in range(N)]
# min_cost = 10000000
#
# all_path_list = list(permutations(list(range(N)), N))
#
#
# def check_cost(N, path):
#     cost = 0
#     path += (path[0],)
#     for i in range(N):
#         if W[path[i]][path[i + 1]] == 0:
#             return 4000000
#         cost += W[path[i]][path[i + 1]]
#
#     return cost
#
#
# for path in all_path_list:
#     min_cost = min(min_cost, check_cost(N, path))
#
# print(min_cost)

import sys

input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().strip().split())) for _ in range(N)]

temp = []
visited = [False] * N
cost_list = []
def dfs(depth):
    if depth == N:
        temp.append(temp[0])
        sum_cost = 0
        for i in range(N):
            if W[temp[i]][temp[i+1]] == 0:
                return
            sum_cost += W[temp[i]][temp[i+1]]
        cost_list.append(sum_cost)
        temp.pop()
        return

    for i in range(N):
        if not visited[i]:
            temp.append(i)
            visited[i] = True
            dfs(depth+1)
            visited[i] = False
            temp.pop()

dfs(0)

print(min(cost_list))

