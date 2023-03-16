import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
minHeap = []
maxHeap = []

for _ in range(N):
    n = int(input().strip())
    if n == 0:
        if len(minHeap) == 0 and len(maxHeap) == 0:
            print(0)
        elif len(minHeap) == 0:
            print(-heapq.heappop(maxHeap))
        elif len(maxHeap) == 0:
            print(heapq.heappop(minHeap))
        else:
            minX = heapq.heappop(minHeap)
            maxX = heapq.heappop(maxHeap)
            if minX < maxX:
                print(minX)
                heapq.heappush(maxHeap, maxX)
            else:
                print(-maxX)
                heapq.heappush(minHeap, minX)
    else:
        if n < 0:
            heapq.heappush(maxHeap, -n)
        else:
            heapq.heappush(minHeap, n)
