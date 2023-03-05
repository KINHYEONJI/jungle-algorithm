num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for score in scores[1:]:
        if score > avg:
            cnt += 1
    print(f'{cnt / scores[0] * 100:.3f}%')
