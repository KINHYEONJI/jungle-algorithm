import sys

input = sys.stdin.readline

N = int(input().strip())

num_list = [list(map(int, input().strip().split())) for _ in range(N)]

num_list.sort(key=lambda x: (x[0], x[1]))

for num in num_list:
    print(num[0], num[1])
