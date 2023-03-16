import sys

input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    list_ = input().strip()
    stack_ = 0
    for i in range(len(list_)):
        if list_[i] == '(':
            stack_ += 1
        else:
            stack_ -= 1
            if stack_ < 0:
                print("NO")
                break

    if stack_ == 0:
        print("YES")

    if stack_ > 0:
        print("NO")
