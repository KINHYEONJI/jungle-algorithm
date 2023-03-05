import sys

input = sys.stdin.readline

N, r, c = map(int, input().strip().split())
num = 0;


def find_Num(N, r, c):
    global num

    if (N == 0):
        print(num)
        return

    n = (2 ** N) // 2

    if r < n and c < n:
        find_Num(N - 1, r, c)
    elif r < n and c >= n:
        num += n * n
        find_Num(N - 1, r, c - n)
    elif r >= n and c < n:
        num += (n * n * 2)
        find_Num(N - 1, r - n, c)
    elif r >= n and c >= n:
        num += (n * n * 3)
        find_Num(N - 1, r - n, c - n)


find_Num(N, r, c)
