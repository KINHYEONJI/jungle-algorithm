import sys

input = sys.stdin.readline

n = int(input().rstrip())
times = []
for _ in range(n):
    s, e = map(int, input().rstrip().split())
    times.append([s, e])

times.sort(key=lambda x: (x[1], x[0]))

count = 1
finish = times[0][1]
for s, e in times[1:n]:
    if s >= finish:
        count += 1
        finish = e

print(count)
