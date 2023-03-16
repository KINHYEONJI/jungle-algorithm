import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

poketmon_int_key = {}
poketmon_name_key = {}

for i in range(N):
    name = input().strip()

    poketmon_int_key[i] = name
    poketmon_name_key[name] = i

for _ in range(M):
    info = input().strip()

    if info.isdigit() == True:
        print(poketmon_int_key[int(info) - 1])
    else:
        print(poketmon_name_key[info] + 1)
