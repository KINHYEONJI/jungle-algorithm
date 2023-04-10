import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
miss_rock = set([int(input().rstrip()) for _ in range(m)])
if 2 in miss_rock:
    print(-1)
    sys.exit()
dp = [sys.maxsize for _ in range(n + 1)]
dp[1] = 0
dp[2] = 1
q = deque([])
q.append((2, 1, 1))
visited = set([(2, 1)])
while q:
    now, move, count = q.popleft()

    if now + move + 1 <= n and now + move + 1 not in miss_rock and (now + move + 1, move + 1) not in visited:
        q.append((now + move + 1, move + 1, count + 1))
        visited.add((now + move + 1, move + 1))
        dp[now + move + 1] = min(dp[now + move + 1], count + 1)
    if now + move <= n and now + move not in miss_rock and (now + move, move) not in visited:
        q.append((now + move, move, count + 1))
        visited.add((now + move, move))
        dp[now + move] = min(dp[now + move], count + 1)
    if move != 1 and now + (move - 1) <= n and now + (move - 1) not in miss_rock and (
            now + (move - 1), move - 1) not in visited:
        q.append((now + (move - 1), move - 1, count + 1))
        visited.add((now + (move - 1), move - 1))
        dp[now + (move - 1)] = min(dp[now + (move - 1)], count + 1)

if dp[n] == sys.maxsize:
    print(-1)
else:
    print(dp[n])
