import sys

input = sys.stdin.readline

N, K = map(int, input().strip().split())
num = list(input().strip())

stack = []

for i in range(0, N):

    while len(stack) > 0 and stack[-1] < num[i] and K > 0:
        stack.pop()
        K -= 1

    stack.append(num[i])

if K != 0:
    while K > 0:
        stack.pop()
        K -= 1

print("".join(stack))
