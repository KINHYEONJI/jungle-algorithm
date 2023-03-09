# heights = [int(input().strip()) for _ in range(9)]
# sum = sum(heights)
#
# for i in range(8):
#     for j in range(i + 1, 9):
#         if sum - heights[i] - heights[j] == 100:
#             del1 = heights[i]
#             del2 = heights[j]
#
# heights.remove(del1)
# heights.remove(del2)
#
# print(*(sorted(heights)), sep='\n')

import sys

input = sys.stdin.readline

heights = sorted(list((int(input().strip())) for _ in range(9)))

answer = []


def dfs(depth):
    if depth == 7:
        if sum(answer) == 100:
            for key in answer:
                print(key)
            sys.exit(0)
        return

    for i in range(depth, 9):
        answer.append(heights[i])
        dfs(depth + 1)
        answer.pop()


dfs(0)
