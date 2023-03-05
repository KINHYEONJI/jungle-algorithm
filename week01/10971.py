import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().strip().split())) for _ in range(N)]
min_cost = 10000000

all_path_list = list(permutations(list(range(N)), N))


def check_cost(N, path):
    cost = 0
    path += (path[0],)
    for i in range(N):
        if W[path[i]][path[i + 1]] == 0:
            return 4000000
        cost += W[path[i]][path[i + 1]]

    return cost


for path in all_path_list:
    min_cost = min(min_cost, check_cost(N, path))

print(min_cost)
