import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().strip().split())
card_list = list(map(int, input().strip().split()))
max_sum = 0

for cards in combinations(card_list, 3):
    if (max_sum < sum(cards) <= m):
        max_sum = sum(cards)

print(max_sum)
