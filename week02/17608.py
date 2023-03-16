import sys

input = sys.stdin.readline

N = int(input().strip())
nums = list(int(input().strip()) for _ in range(N))
nums.reverse()

stack = [nums[0]]
for i in range(1, N):
    if nums[i] > stack[-1]:
        stack.append(nums[i])

print(len(stack))
