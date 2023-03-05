import sys

input = sys.stdin.readline

N = int(input())
w = set(input().strip() for _ in range(N))

w_list = list(w)

w_list.sort()
w_list.sort(key=len)

for i in range(len(w_list)):
    print(w_list[i])
