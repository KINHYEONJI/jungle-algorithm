num = 1
for _ in range(3):
    num *= int(input())

for i in range(10):
    print(list(str(num)).count(str(i)))
