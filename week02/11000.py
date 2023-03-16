import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())

time_table = sorted(list(map(int, input().strip().split())) for _ in range(N))
room = []
heapq.heappush(room, time_table[0][1])

for i in range(1, N):
    if time_table[i][0] < room[0]:
        heapq.heappush(room, time_table[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time_table[i][1])

print(len(room))
