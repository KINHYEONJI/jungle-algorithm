import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().strip().split()))
max_sum = 0

for cards in permutations(card_list, n):
    sum = 0
    for i in range(1, n):
        sum += abs((cards[i - 1] - cards[i]))

    if (max_sum < sum):
        max_sum = sum

print(max_sum)
