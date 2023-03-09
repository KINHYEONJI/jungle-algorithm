import sys
from collections import Counter

input = sys.stdin.readline

N = int(input().strip())

num_list = sorted(list(int(input().strip()) for _ in range(N)))

print(round(sum(num_list) / N))

print(num_list[N // 2])

count = Counter(num_list).most_common()
if len(count) == 1:
    print(count[0][0])
elif count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(max(num_list) - min(num_list))
