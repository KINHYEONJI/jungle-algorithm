import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = list(int(input().rstrip()) for _ in range(n))
visited = [False] * (k + 1)
q = deque()
q.append([0, 0])


def find():
    while q:
        count, money = q.popleft()

        for i in range(n):
            if money + coins[i] > k:
                continue
            if money + coins[i] == k:
                return count + 1
            if not visited[money + coins[i]]:
                q.append([count + 1, money + coins[i]])
                visited[money + coins[i]] = True

    return -1


print(find())
