def is_hansu(num):
    num_list = list(map(int, str(num)))
    if (num_list[1] - num_list[2]) == (num_list[0] - num_list[1]):
        return True
    else:
        return False


num = int(input())

if num < 100:
    print(num)
else:
    count = 99
    for i in range(100, num + 1):
        if is_hansu(i):
            count += 1
    print(count)
