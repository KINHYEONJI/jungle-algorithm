cnt = int(input())

for _ in range(cnt):
    num, str = input().split()
    answer = ''
    for x in str:
        answer += x * int(num)
    print(answer)
