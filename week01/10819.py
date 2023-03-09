# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# n = int(input())
# card_list = list(map(int, input().strip().split()))
# max_sum = 0
#
# for cards in permutations(card_list, n):
#     sum = 0
#     for i in range(1, n):
#         sum += abs((cards[i - 1] - cards[i]))
#
#     if (max_sum < sum):
#         max_sum = sum
#
# print(max_sum)

import sys

input = sys.stdin.readline

def dfs(depth):
    if depth  == N :
        sum_list.append(sum(abs(num_list[i+1]-num_list[i]) for i in range(N-1)))
        return

    for i in range(N):
        if not visited[i] :
            num_list.append(card_list[i])
            visited[i] = True
            dfs(depth+1)
            visited[i] = False
            num_list.pop()

N = int(input())
card_list = list(map(int, input().strip().split()))
num_list = []
sum_list = []
visited = [False] * N
dfs(0)
print(max(sum_list))
