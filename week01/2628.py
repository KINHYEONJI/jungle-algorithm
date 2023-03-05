x, y = map(int, input().split())
num = int(input())

x_list = [0, y]
y_list = [0, x]

for _ in range(num):
    xy, line_num = map(int, input().split())
    if (xy == 0):
        x_list.append(line_num)
    elif (xy == 1):
        y_list.append(line_num)

x_max = 0
y_max = 0

x_list.sort()
y_list.sort()

x_max = 0
y_max = 0

for i in range(len(x_list) - 1, 0, -1):
    if (x_list[i] - x_list[i - 1] > x_max):
        x_max = x_list[i] - x_list[i - 1]

for i in range(len(y_list) - 1, 0, -1):
    if (y_list[i] - y_list[i - 1] > y_max):
        y_max = y_list[i] - y_list[i - 1]

print(x_max * y_max)
