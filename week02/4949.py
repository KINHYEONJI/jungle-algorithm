import sys

input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    stack = []

    if sentence == ".":
        break

    for str in sentence:
        if str == '[' or str == '(':
            stack.append(str)
        elif str == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif str == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
