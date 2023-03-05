n = int(input())

for _ in range(n):
    str = input()
    score = 0
    sum_score = 0
    for i in range(len(str)):
        if str[i] == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
