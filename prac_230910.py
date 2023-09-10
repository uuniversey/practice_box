
import sys
sys.stdin = open('wj.txt', 'r')


# 백준. 1260 DFS와 BFS
#
# def dfs(adj_l, s):
#     for j in adj_l[s]:
#         if vstd_d[j] == 0:
#             stack.append(j)
#             vstd_d[j] = 1
#             dfs(adj_l, j)
#
# def bfs(adj_l, s):
#     queue = [s]
#     while queue:
#         t = queue.pop(0)
#         if vstd_b[t] == 0:
#             result.append(t)
#             vstd_b[t] = 1
#             for i in adj_l[t]:
#                 queue.append(i)
#     return result
#
#
# N, M, V = map(int, input().split())
# adj_l = [[] for _ in range(N+1)]
# vstd_d = [0] * (N+1)
# vstd_b = [0] * (N+1)
# stack = [V]
# vstd_d[V] = 1
# result = [V]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     adj_l[a].append(b)
#     adj_l[b].append(a)
#
# for li in adj_l:
#     li.sort()
#
# dfs(adj_l, V)
# bfs(adj_l, V)
#
# print(*stack)
# print(*result[1:])


# 백준. 17471 게리맨더링

from collections import deque

def bfs(adj_l, s):
    deq = deque([s])
    vstd[s] = 1
    while deq:
        t = deq.popleft()
        for j in adj_l[t]:
            if vstd[j] == 0:
                vstd[j] = vstd[t] + 1
                deq.append(j)


N = int(input())
citizen = list(map(int, input().split()))
adj_l = [[] for _ in range(N+1)]
vstd = [0] * (N+1)
for i in range(1, N+1):
    adj_l[i] = list(map(int, input().split()))[1:]

bfs(adj_l, 1)

print()