heights = [int(input().strip()) for _ in range(9)]
sum = sum(heights)

for i in range(8):
    for j in range(i + 1, 9):
        if sum - heights[i] - heights[j] == 100:
            del1 = heights[i]
            del2 = heights[j]

heights.remove(del1)
heights.remove(del2)

print(*(sorted(heights)), sep='\n')
