def dfs(depth, index, n, m):
    global max_sum
    if depth == 3 :
        if max_sum < sum(temp) <= m :
            max_sum = sum(temp)
        return

    for i in range(index, n):
        temp.append(card_list[i])
        dfs(depth+1, i+1,  n, m)
        temp.pop()


import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().strip().split())
card_list = sorted(list(map(int, input().strip().split())))
max_sum = 0
# for cards in combinations(card_list, 3):
#     if (max_sum < sum(cards) <= m):
#         max_sum = sum(cards)
#
# print(max_sum)

temp = []


dfs(0, 0, n, m)

print(max_sum)