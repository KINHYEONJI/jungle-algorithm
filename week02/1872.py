import sys

input = sys.stdin.readline

N = int(input().strip())
nums = list(int(input().strip()) for _ in range(N))

stack = []
arr = []
answer = []

last_num = 0

for i in range(N):
    while nums[i] not in stack:
        last_num += 1
        
        if last_num > N:
            print("NO")
            sys.exit()

        stack.append(last_num)
        answer.append("+")

    arr.append(stack.pop())
    answer.append("-")

print(*answer, sep="\n")
