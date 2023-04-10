import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
count = [[i + 1, 0] for i in range(k)]

input_list = list(map(int, input().rstrip().split()))
multitap = []
count = 0

for i in range(k):

    if input_list[i] in multitap:  # 들어갈 숫자가 멀티탭에 이미 있다면 continue
        continue

    if len(multitap) < n:  # 멀티탭의 길이가 n보다 적으면(더 꼽을수 있으면) 멀티탭에 추가
        multitap.append(input_list[i])
        continue

    temp = []
    for num in multitap:
        if num not in input_list[i:]:
            temp.append([num, k + 1])

        else:
            temp.append([num, input_list[i::].index(num)])

    temp.sort(key=lambda x: -x[1])

    multitap[multitap.index(temp[0][0])] = input_list[i]
    count += 1

print(count)
