import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

q = deque()

for _ in range(N):
    command = input().strip()

    if command == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif command == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    else:
        command, num = command.split()
        q.append(num)
