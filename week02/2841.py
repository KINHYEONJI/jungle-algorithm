import sys

input = sys.stdin.readline

N, P = map(int, input().strip().split())

stack = [[] for _ in range(P + 1)]
count = 0
for _ in range(N):
    line, flet = map(int, input().strip().split())

    while len(stack[line]) != 0 and stack[line][-1] > flet:
        stack[line].pop()
        count += 1

    if len(stack[line]) == 0:
        stack[line].append(flet)
        count += 1
        continue

    if stack[line][-1] < flet:
        stack[line].append(flet)
        count += 1

print(count)
