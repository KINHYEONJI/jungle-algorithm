import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

temp= []

def dfs(depth) :
    if(depth == M) :
        print(' '.join(map(str, temp)))
        return

    for i in range(1, N+1) :
        if i not in temp :
            temp.append(i)
            dfs(depth+1)
            temp.pop()

dfs(0)

