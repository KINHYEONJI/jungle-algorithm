import sys

input = sys.stdin.readline

A, B, C = map(int, input().strip().split())


def recursion(A, B, C):
    if B == 1:
        return A % C
    if B % 2 != 0:
        return (recursion(A, B // 2, C) * recursion(A, B // 2 + 1, C)) % C
    else:
        return (recursion(A, B // 2, C) ** 2) % C


print(recursion(A, B, C))
