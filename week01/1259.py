import sys

input = sys.stdin.readline

while (1):
    word = input().strip()

    if word == '0':
        break

    if word[::-1] == word:
        print("yes")
    else:
        print("no")
