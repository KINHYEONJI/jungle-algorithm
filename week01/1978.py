n = int(input())
numbers = list(map(int, input().split()))
resCnt = 0

for number in numbers:
    cnt = 0
    if number == 1:
        continue

    for i in range(2, number + 1):
        if number % i == 0:
            cnt += 1

    if cnt == 1:
        resCnt += 1

print(resCnt)
