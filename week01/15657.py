import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
num_list = list(map(int, input().strip().split()))

temp= []

num_list.sort()
def dfs(depth, index):
    if(depth == M) :
        print(' '.join(map(str, temp)))
        return

    for i in range(index, N) :
        temp.append(num_list[i])
        dfs(depth+1, i)
        temp.pop()

dfs(0 ,0)
