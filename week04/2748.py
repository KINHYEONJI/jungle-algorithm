import sys

input = sys.stdin.readline

num = int(input().rstrip())

fibo = [0, 1]
for i in range(2, num + 1):
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[-1])
