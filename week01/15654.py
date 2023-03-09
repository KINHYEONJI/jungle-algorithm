import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
num_list = list(map(int, input().strip().split()))
temp= []

num_list.sort()

def dfs(depth) :
    if(depth == M) :
        print(' '.join(map(str, temp)))
        return

    for i in range(0, N):
        if num_list[i] not in temp :
            temp.append(num_list[i])
            dfs(depth+1)
            temp.pop()

dfs(0)
