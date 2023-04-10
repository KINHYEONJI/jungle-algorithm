import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    score = []
    for _ in range(n):
        score.append(list(map(int, input().rstrip().split())))

    score.sort(key=lambda x: (x[0]))
    count = n
    a_max, b_max = score[0][0], score[0][1]
    for i in range(1, n):
        if a_max < score[i][0] and b_max < score[i][1]:
            count -= 1
        else:
            a_max = score[i][0]
            b_max = score[i][1]

    print(count)
