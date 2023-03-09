import sys
from collections import Counter

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().strip().split()))
M = int(input().strip())
find_cards = list(map(int, input().strip().split()))

c = Counter(cards)

for i in find_cards:
    if i in c:
        print(c[i], end=" ")
    else:
        print(0, end=" ")
