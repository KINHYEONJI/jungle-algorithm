import sys

input = sys.stdin.readline

N = int(input().strip())

stack_ = []

for _ in range(N):
    num = int(input().strip())

    if num == 0:
        stack_.pop()

    else:
        stack_.append(num)

print(sum(stack_))
