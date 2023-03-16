import sys

input = sys.stdin.readline

N = int(input().strip())
costs = sorted(list(map(int, input().strip().split())))
budget = int(input())

if sum(costs) <= budget:
    print(costs[-1])

else:
    start = 1
    end = costs[-1]

    while start <= end:
        mid = (start + end) // 2
        sum_cost = 0
        for cost in costs:
            if mid <= cost:
                sum_cost += mid
            else:
                sum_cost += cost

        if sum_cost <= budget:
            start = mid + 1
        else:
            end = mid - 1

    print(end)
