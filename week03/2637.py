import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input().rstrip())
connect = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
needs = [[0] * (n + 1) for _ in range(n + 1)]
base = []
q = deque()
for _ in range(m):
    x, y, k = map(int, input().rstrip().split())
    connect[y].append([x, k])
    degree[x] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    idx = q.popleft()
    for part in connect[idx]:
        if needs[idx].count(0) == n + 1:
            needs[part[0]][idx] += part[1]
        else:
            for i in range(1, n + 1):
                needs[part[0]][i] += needs[idx][i] * part[1]
        degree[part[0]] -= 1
        if degree[part[0]] == 0:
            q.append(part[0])

for i in range(1, n + 1):
    if needs[n][i] != 0:
        print(i, needs[n][i])
# import sys
#
# input = sys.stdin.readline
#
# n = int(input().rstrip())
# m = int(input().rstrip())
# needs = [[] for _ in range(n + 1)]
# count = [0 for _ in range(n + 1)]
#
# for _ in range(m):
#     x, y, k = map(int, input().rstrip().split())
#     needs[x].append([y, k])
#
#
# def dfs(need, num):
#     for part in need:
#         if len(needs[part[0]]) == 0:
#             count[part[0]] += part[1] * num
#
#         else:
#             dfs(needs[part[0]], part[1] * num)
#
#
# dfs(needs[n], 1)
#
# for i in range(1, n + 1):
#     if count[i] != 0:
#         print(i, count[i])
