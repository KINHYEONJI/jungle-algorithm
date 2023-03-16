import sys

input = sys.stdin.readline

strs = list(input().strip())
temp = []

M = int(input().strip())

for i in range(M):
    command = input().strip()

    if command == "L":
        if strs:
            temp.append(strs.pop())
    elif command == "D":
        if temp:
            strs.append(temp.pop())
    elif command == "B":
        if strs:
            strs.pop()
    else:
        P, str = command.split()
        strs.append(str)

while temp:
    strs.append(temp.pop())
print("".join(strs))
