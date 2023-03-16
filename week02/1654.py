import sys

input = sys.stdin.readline

K, N = map(int, input().strip().split())
lan_lines = sorted(list(int(input().strip()) for _ in range(K)))

start = 1
end = lan_lines[-1]

while start <= end:

    mid = (start + end) // 2
    count = 0
    for lan_line in lan_lines:
        count += (lan_line // mid)
        
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
