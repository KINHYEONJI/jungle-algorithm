import sys

input = sys.stdin.readline

N = int(input().strip())
N_list = sorted(list(map(int, input().strip().split())))
M = int(input().strip())
M_list = list(map(int, input().strip().split()))


def binary(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return 1

    elif arr[mid] > target:
        return binary(arr, target, start, mid - 1)

    elif arr[mid] < target:
        return binary(arr, target, mid + 1, end)


for m in M_list:
    print(binary(N_list, m, 0, N - 1))
