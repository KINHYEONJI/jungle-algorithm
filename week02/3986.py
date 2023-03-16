import sys

input = sys.stdin.readline

N = int(input().strip())
count = 0
for _ in range(N):
    str = list(input().strip())
    stack = []

    for i in range(len(str)):
        if len(stack) != 0 and str[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(str[i])

    if len(stack) == 0:
        count += 1

print(count)
