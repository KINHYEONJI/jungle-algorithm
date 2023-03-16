import sys

input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    str = input().strip()
    stack = []
    temp = []
    for i in range(len(str)):
        if str[i] == "<":
            if stack:
                temp.append(stack.pop())
        elif str[i] == ">":
            if temp:
                stack.append(temp.pop())
        elif str[i] == "-":
            if stack:
                stack.pop()
        else:
            stack.append(str[i])
            
    while temp:
        stack.append(temp.pop())
    print("".join(stack))
