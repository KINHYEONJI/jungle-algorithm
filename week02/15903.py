import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
hq = []
for num in numbers:
    heapq.heappush(hq, num)

for _ in range(m):
    num = heapq.heappop(hq) + heapq.heappop(hq)
    heapq.heappush(hq, num)
    heapq.heappush(hq, num)

print(sum(hq))
