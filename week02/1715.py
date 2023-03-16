import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    heapq.heappush(hq, int(input().strip()))
sum_ = 0
while len(hq) > 1:
    temp = heapq.heappop(hq) + heapq.heappop(hq)
    sum_ += temp
    heapq.heappush(hq, temp)

print(sum_)
