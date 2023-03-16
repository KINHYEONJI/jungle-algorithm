import sys, heapq

input = sys.stdin.readline

N = int(input().strip())
mid = -sys.maxsize
maxHeap = []
minHeap = []

for _ in range(N):
    n = int(input().strip())

    if mid < n:
        heapq.heappush(minHeap, n)
    else:
        heapq.heappush(maxHeap, -n)

    if len(minHeap) - len(maxHeap) > 1:
        heapq.heappush(maxHeap, -heapq.heappop(minHeap))
    elif len(maxHeap) - len(minHeap) > 1:
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))

    if len(minHeap) > len(maxHeap):
        mid = minHeap[0]
        print(mid)
    elif len(minHeap) < len(maxHeap):
        mid = -maxHeap[0]
        print(mid)
    elif len(minHeap) == len(maxHeap):
        print(-maxHeap[0])
        mid = (-maxHeap[0] + minHeap[0]) / 2

# n = int(sys.stdin.readline())
#
# leftHeap = []
# rightHeap = []
# for i in range(n):
#     num = int(sys.stdin.readline())
#
#     if len(leftHeap) == len(rightHeap):
#         heapq.heappush(leftHeap, -num)
#     else:
#         heapq.heappush(rightHeap, num)
#
#     if rightHeap and rightHeap[0] < -leftHeap[0]:
#         leftValue = heapq.heappop(leftHeap)
#         rightValue = heapq.heappop(rightHeap)
#
#         heapq.heappush(leftHeap, -rightValue)
#         heapq.heappush(rightHeap, -leftValue)
#
#     print(-leftHeap[0])
