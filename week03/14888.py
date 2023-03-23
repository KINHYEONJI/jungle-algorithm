import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
op = list(map(int, input().rstrip().split()))
op_list = ""
min = sys.maxsize
max = -sys.maxsize
temp = []

for i in range(4):
    if i == 0:
        op_list += "+" * op[i]
    elif i == 1:
        op_list += "-" * op[i]
    elif i == 2:
        op_list += "*" * op[i]
    elif i == 3:
        op_list += "/" * op[i]

op_list = list(op_list)
visited = [False] * (N - 1)


def dfs(depth, op_list):
    global min, max
    if depth == N - 1:
        result = numbers[0]
        for i in range(N - 1):
            if temp[i] == "+":
                result += numbers[i + 1]
            elif temp[i] == "-":
                result -= numbers[i + 1]
            elif temp[i] == "*":
                result *= numbers[i + 1]
            elif temp[i] == "/":
                if result < 0:
                    result = -(abs(result) // numbers[i + 1])
                else:
                    result //= numbers[i + 1]

        if min > result:
            min = result

        if max < result:
            max = result
        return

    for i in range(N - 1):
        if visited[i] == False:
            visited[i] = True
            temp.append(op_list[i])
            dfs(depth + 1, op_list)
            temp.pop()
            visited[i] = False


dfs(0, op_list)
print(max)
print(min)
