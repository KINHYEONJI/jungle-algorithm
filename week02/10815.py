import sys

input = sys.stdin.readline

N = int(input().strip())
N_list = sorted(list(map(int, input().strip().split())))
M = int(input().strip())
M_list = list(map(int, input().strip().split()))
answer = []


def is_include(list, num):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if list[mid] <= num:
            start = mid + 1
        else:
            end = mid - 1

    if list[end] == num:
        answer.append("1")
    else:
        answer.append("0")


for m in M_list:
    is_include(N_list, m)

print(*answer)
