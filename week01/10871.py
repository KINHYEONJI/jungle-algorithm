n, x = map(int, input().split())

datas = list(map(int, input().split()))

# for i in range(n):
#     if int(data[i]) < x:
#         print(data[i], end=" ")

for data in datas:
    if (data < x):
        print(data, end=" ")
