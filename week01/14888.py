import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().strip().split()))
op_num_list = list(map(int, input().strip().split()))
op = ['+', '-', '*', '//']
op_list = []

for i in range(4):
    for j in range(op_num_list[i]):
        op_list.append(op[i])

all_op_permuatioan = set(list(permutations(op_list, len(op_list))))

max_result = -sys.maxsize
min_result = sys.maxsize


def caclutate(num_list, op_permutation):
    result = num_list[0]
    for i in range(len(op_permutation)):
        if (op_permutation[i] == "+"):
            result += num_list[i + 1]
        elif (op_permutation[i] == "-"):
            result -= num_list[i + 1]
        elif (op_permutation[i] == "*"):
            result *= num_list[i + 1]
        elif (op_permutation[i] == "//"):
            result /= num_list[i + 1]
            result = int(result)
    return result


for op_permuation in all_op_permuatioan:
    result = caclutate(num_list, op_permuation)
    min_result = min(min_result, result)
    max_result = max(max_result, result)

print(max_result, min_result)
