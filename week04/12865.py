import sys

N, K = map(int, input().split())
stuffs = []
knapsack = [0 for _ in range(K + 1)]

for _ in range(N):
    stuffs.append(list(map(int, input().split())))

for w, v in stuffs:
    for i in range(K, w - 1, -1):
        if knapsack[i - w] + v > knapsack[i]:
            knapsack[i] = knapsack[i - w] + v
print(knapsack[K])
