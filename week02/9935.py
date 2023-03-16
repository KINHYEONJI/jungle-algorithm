# import sys
#
# input = sys.stdin.readline
#
# str = input().strip()
# find_str = input().strip()
# stack = []
#
# for i in range(len(str)):
#     stack.append(str[i])
#     if find_str in "".join(stack):
#         j = 0
#         while j < len(find_str):
#             stack.pop()
#             j += 1
#
# if len(stack) == 0:
#     print("FRULA")
# else:
#     print("".join(stack))
import sys

input = sys.stdin.readline

str = input().strip()
find_str = input().strip()
stack = []
find_str_len = len(find_str)

for i in range(len(str)):
    stack.append(str[i])
    if stack[-find_str_len:] == list(find_str):
        del stack[-find_str_len:]

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
