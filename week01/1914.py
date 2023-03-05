def hanoi(i, a, c, b):
    if (i == 1):
        print(a, c, sep=" ")
    else:
        hanoi(i - 1, a, b, c)
        hanoi(1, a, c, b)
        hanoi(i - 1, b, c, a)


n = int(input())
print(2 ** n - 1)
if (n <= 20):
    hanoi(n, 1, 3, 2)
