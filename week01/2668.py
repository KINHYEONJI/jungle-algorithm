import sys

input = sys.stdin.readline

N = int(input().strip())
num_list = [[0, 0]] + [[i, int(input().strip())] for i in range(1, N + 1)]

answer = []
visited = [False] * (N + 1)


def dfs(index):
    temp.append(index)
    if num_list[index][1] == temp[0]:
        visited[index] = True
        return True

    if (visited[index] == True) or (num_list[index][1] in temp):
        return False

    visited[index] = True

    if dfs(num_list[index][1]):
        return True

    visited[index] = False


for i in range(1, N + 1):
    temp = []
    if dfs(i) == True:
        answer.append(temp)

sorted_answer = sorted([val for row in answer for val in row])

print(len(sorted_answer), *sorted_answer, sep="\n")
