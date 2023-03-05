from itertools import permutations

n = int(input())
k = int(input())
card_list = []

for _ in range(n):
    card = input()
    card_list.append(card)

result = set()

for i in permutations(card_list, k):
    result.add(''.join(i))

print(len(result))
