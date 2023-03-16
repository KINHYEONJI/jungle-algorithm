import sys

input = sys.stdin.readline

string = input().strip()
stack = []
flag = False
res = ''

for s in string:
    if s == " ":
        while stack:
            res += stack.pop()
        res += s
    elif s == "<":
        while stack:
            res += stack.pop()
        flag = True
        res += s
    elif s == ">":
        flag = False
        res += s
    elif flag:
        res += s
    else:
        stack.append(s)

while stack:
    res += stack.pop()

print(res)

# import sys
#
# input = sys.stdin.readline
#
# str = list(input().strip())
#
# stack = []
# temp = []
# answer = []
# flag = 0
# for i in range(len(str)):
#     if str[i] == "<":
#         flag = 1
#         answer.append(str[i])
#         continue
#     elif str[i] == ">":
#         flag = 0
#         answer.append(str[i])
#         continue
#
#     if flag == 1:
#         answer.append(str[i])
#     elif
#
#
# print(str)
