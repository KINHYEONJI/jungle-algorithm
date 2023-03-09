import sys

input = sys.stdin.readline

N = int(input().strip())

num_list = [list(map(int, input().strip().split())) for i in range(N)]

num_list.sort(key=lambda x: (x[1], x[0]))

for num in num_list:
    print(num[0], num[1])
