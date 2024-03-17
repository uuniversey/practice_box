
import sys
sys.stdin = open('test.txt')

# 백준. 1967 트리의 지름


def dfs(s, d):
    for i in Tree[s]:
        idx, val = i
        if not vstd[idx]:
            vstd[idx] = d + val
            dfs(idx, vstd[idx])


sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
Tree = [[] for _ in range(n+1)]
vstd = [0] * (n+1)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    Tree[a].append((b, c))
    Tree[b].append((a, c))

vstd[1] = 1
dfs(1, 1)


point = vstd.index(max(vstd))
vstd = [0] * (n+1)
vstd[point] = 1
dfs(point, 1)

print(max(vstd)-1)