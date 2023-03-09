import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

temp = []


def dfs(depth, before):
    if(depth == M) :
        print(' '.join(map(str, temp)))
        return

    for i in range(before+1, N+1) :
        temp.append(i)
        dfs(depth+1, i)
        temp.pop()


dfs(0, 0)

