import sys

input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().strip().split()))

stack = []
answer = [-1] * N

for i in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack[-1]] = numbers[i]
        stack.pop()
    stack.append(i)

print(*answer)

# import sys
#
# input = sys.stdin.readline
#
# N = int(input().strip())
# numbers = list(map(int, input().strip().split()))
#
# stack = []
# answer = []
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         if len(stack) == 0:
#             if numbers[j] > numbers[i]:
#                 stack.append(numbers[j])
#
#             elif numbers[j] < numbers[i]:
#                 continue
#
#         elif numbers[i] < numbers[j] < stack[-1]:
#             stack.pop()
#             stack.append(numbers[j])
#
#     if len(stack) == 0:
#         answer.append(-1)
#     else:
#         answer.append(stack[-1])
#     stack = []
# answer.append(-1)
# print(*answer)
